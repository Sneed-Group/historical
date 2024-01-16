/*
 * ARM SBSA Reference Platform emulation-based PCI
 *
 * Copyright (c) 2018 Linaro Limited
 * Copyright (c) 2023 Samuel Lord
 * Written by Hongbo Zhang <hongbo.zhang@linaro.org>
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms and conditions of the GNU General Public License,
 * version 2 or later, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "qemu/osdep.h"
#include "qemu-common.h"
#include "qapi/error.h"
#include "qemu/error-report.h"
#include "qemu/units.h"
#include "sysemu/device_tree.h"
#include "sysemu/numa.h"
#include "sysemu/runstate.h"
#include "sysemu/sysemu.h"
#include "exec/address-spaces.h"
#include "exec/hwaddr.h"
#include "kvm_arm.h"
#include "hw/arm/boot.h"
#include "hw/block/flash.h"
#include "hw/boards.h"
#include "hw/ide/internal.h"
#include "hw/ide/ahci_internal.h"
#include "hw/intc/arm_gicv3_common.h"
#include "hw/loader.h"
#include "hw/pci-host/gpex.h"
#include "hw/qdev-properties.h"
#include "hw/usb.h"
#include "hw/char/pl011.h"
#include "net/net.h"

#define RAMLIMIT_GB 8192
#define RAMLIMIT_BYTES (RAMLIMIT_GB * GiB)

#define NUM_IRQS        256
#define NUM_SMMU_IRQS   4
#define NUM_SATA_PORTS  6

#define VIRTUAL_PMU_IRQ        7
#define ARCH_GIC_MAINT_IRQ     9
#define ARCH_TIMER_VIRT_IRQ    11
#define ARCH_TIMER_S_EL1_IRQ   13
#define ARCH_TIMER_NS_EL1_IRQ  14
#define ARCH_TIMER_NS_EL2_IRQ  10

enum {
    SBSA_FLASH,
    SBSA_MEM,
    SBSA_CPUPERIPHS,
    SBSA_GIC_DIST,
    SBSA_GIC_REDIST,
    SBSA_SMMU,
    SBSA_UART,
    SBSA_RTC,
    SBSA_PCIE,
    SBSA_PCIE_MMIO,
    SBSA_PCIE_MMIO_HIGH,
    SBSA_PCIE_PIO,
    SBSA_PCIE_ECAM,
    SBSA_GPIO,
    SBSA_SECURE_UART,
    SBSA_SECURE_UART_MM,
    SBSA_SECURE_MEM,
    SBSA_AHCI,
    SBSA_EHCI,
};

typedef struct MemMapEntry {
    hwaddr base;
    hwaddr size;
} MemMapEntry;

typedef struct {
    MachineState parent;
    struct arm_boot_info bootinfo;
    int smp_cpus;
    void *fdt;
    int fdt_size;
    int psci_conduit;
    DeviceState *gic;
    PFlashCFI01 *flash[2];
} SBSAMachineState;

#define TYPE_SBSA_MACHINE   MACHINE_TYPE_NAME("sbsa-ref")
#define SBSA_MACHINE(obj) \
    OBJECT_CHECK(SBSAMachineState, (obj), TYPE_SBSA_MACHINE)

static const MemMapEntry sbsa_ref_memmap[] = {
    /* 512M boot ROM */
    [SBSA_FLASH] =              {          0, 0x20000000 },
    /* 512M secure memory */
    [SBSA_SECURE_MEM] =         { 0x20000000, 0x20000000 },
    /* Space reserved for CPU peripheral devices */
    [SBSA_CPUPERIPHS] =         { 0x40000000, 0x00040000 },
    [SBSA_GIC_DIST] =           { 0x40060000, 0x00010000 },
    [SBSA_GIC_REDIST] =         { 0x40080000, 0x04000000 },
    [SBSA_UART] =               { 0x60000000, 0x00001000 },
    [SBSA_RTC] =                { 0x60010000, 0x00001000 },
    [SBSA_GPIO] =               { 0x60020000, 0x00001000 },
    [SBSA_SECURE_UART] =        { 0x60030000, 0x00001000 },
    [SBSA_SECURE_UART_MM] =     { 0x60040000, 0x00001000 },
    [SBSA_SMMU] =               { 0x60050000, 0x00020000 },
    /* Space here reserved for more SMMUs */
    [SBSA_AHCI] =               { 0x60100000, 0x00010000 },
    [SBSA_EHCI] =               { 0x60110000, 0x00010000 },
    /* Space here reserved for other devices */
    [SBSA_PCIE_PIO] =           { 0x7fff0000, 0x00010000 },
    /* 32-bit address PCIE MMIO space */
    [SBSA_PCIE_MMIO] =          { 0x80000000, 0x70000000 },
    /* 256M PCIE ECAM space */
    [SBSA_PCIE_ECAM] =          { 0xf0000000, 0x10000000 },
    /* ~1TB PCIE MMIO space (4GB to 1024GB boundary) */
    [SBSA_PCIE_MMIO_HIGH] =     { 0x100000000ULL, 0xFF00000000ULL },
    [SBSA_MEM] =                { 0x10000000000ULL, RAMLIMIT_BYTES },
};

static const int sbsa_ref_irqmap[] = {
    [SBSA_UART] = 1,
    [SBSA_RTC] = 2,
    [SBSA_PCIE] = 3, /* ... to 6 */
    [SBSA_GPIO] = 7,
    [SBSA_SECURE_UART] = 8,
    [SBSA_SECURE_UART_MM] = 9,
    [SBSA_AHCI] = 10,
    [SBSA_EHCI] = 11,
};


static void create_ahci(const SBSAMachineState *sms)
{
    hwaddr base = sbsa_ref_memmap[SBSA_AHCI].base;
    int irq = sbsa_ref_irqmap[SBSA_AHCI];
    DeviceState *dev;
    DriveInfo *hd[NUM_SATA_PORTS];
    SysbusAHCIState *sysahci;
    AHCIState *ahci;
    int i;

    dev = qdev_new("sysbus-ahci");
    qdev_prop_set_uint32(dev, "num-ports", NUM_SATA_PORTS);
    sysbus_realize_and_unref(SYS_BUS_DEVICE(dev), &error_fatal);
    sysbus_mmio_map(SYS_BUS_DEVICE(dev), 0, base);
    sysbus_connect_irq(SYS_BUS_DEVICE(dev), 0, qdev_get_gpio_in(sms->gic, irq));

    sysahci = SYSBUS_AHCI(dev);
    ahci = &sysahci->ahci;
    ide_drive_get(hd, ARRAY_SIZE(hd));
    for (i = 0; i < ahci->ports; i++) {
        if (hd[i] == NULL) {
            continue;
        }
        ide_create_drive(&ahci->dev[i].port, 0, hd[i]);
    }
}

static void create_ehci(const SBSAMachineState *sms)
{
    hwaddr base = sbsa_ref_memmap[SBSA_EHCI].base;
    int irq = sbsa_ref_irqmap[SBSA_EHCI];

    sysbus_create_simple("platform-ehci-usb", base,
                         qdev_get_gpio_in(sms->gic, irq));
}

static void create_smmu(const SBSAMachineState *sms, PCIBus *bus)
{
    hwaddr base = sbsa_ref_memmap[SBSA_SMMU].base;
    int irq =  sbsa_ref_irqmap[SBSA_SMMU];
    DeviceState *dev;
    int i;

    dev = qdev_new("arm-smmuv3");

    object_property_set_link(OBJECT(dev), "primary-bus", OBJECT(bus),
                             &error_abort);
    sysbus_realize_and_unref(SYS_BUS_DEVICE(dev), &error_fatal);
    sysbus_mmio_map(SYS_BUS_DEVICE(dev), 0, base);
    for (i = 0; i < NUM_SMMU_IRQS; i++) {
        sysbus_connect_irq(SYS_BUS_DEVICE(dev), i,
                           qdev_get_gpio_in(sms->gic, irq + 1));
    }
}

static void create_pcie(SBSAMachineState *sms)
{
    hwaddr base_ecam = sbsa_ref_memmap[SBSA_PCIE_ECAM].base;
    hwaddr size_ecam = sbsa_ref_memmap[SBSA_PCIE_ECAM].size;
    hwaddr base_mmio = sbsa_ref_memmap[SBSA_PCIE_MMIO].base;
    hwaddr size_mmio = sbsa_ref_memmap[SBSA_PCIE_MMIO].size;
    hwaddr base_mmio_high = sbsa_ref_memmap[SBSA_PCIE_MMIO_HIGH].base;
    hwaddr size_mmio_high = sbsa_ref_memmap[SBSA_PCIE_MMIO_HIGH].size;
    hwaddr base_pio = sbsa_ref_memmap[SBSA_PCIE_PIO].base;
    int irq = sbsa_ref_irqmap[SBSA_PCIE];
    MemoryRegion *mmio_alias, *mmio_alias_high, *mmio_reg;
    MemoryRegion *ecam_alias, *ecam_reg;
    DeviceState *dev;
    PCIHostState *pci;
    int i;

    dev = qdev_new(TYPE_GPEX_HOST);
    sysbus_realize_and_unref(SYS_BUS_DEVICE(dev), &error_fatal);

    /* Map ECAM space */
    ecam_alias = g_new0(MemoryRegion, 1);
    ecam_reg = sysbus_mmio_get_region(SYS_BUS_DEVICE(dev), 0);
    memory_region_init_alias(ecam_alias, OBJECT(dev), "pcie-ecam",
                             ecam_reg, 0, size_ecam);
    memory_region_add_subregion(get_system_memory(), base_ecam, ecam_alias);

    /* Map the MMIO space */
    mmio_alias = g_new0(MemoryRegion, 1);
    mmio_reg = sysbus_mmio_get_region(SYS_BUS_DEVICE(dev), 1);
    memory_region_init_alias(mmio_alias, OBJECT(dev), "pcie-mmio",
                             mmio_reg, base_mmio, size_mmio);
    memory_region_add_subregion(get_system_memory(), base_mmio, mmio_alias);

    /* Map the MMIO_HIGH space */
    mmio_alias_high = g_new0(MemoryRegion, 1);
    memory_region_init_alias(mmio_alias_high, OBJECT(dev), "pcie-mmio-high",
                             mmio_reg, base_mmio_high, size_mmio_high);
    memory_region_add_subregion(get_system_memory(), base_mmio_high,
                                mmio_alias_high);

    /* Map IO port space */
    sysbus_mmio_map(SYS_BUS_DEVICE(dev), 2, base_pio);

    for (i = 0; i < GPEX_NUM_IRQS; i++) {
        sysbus_connect_irq(SYS_BUS_DEVICE(dev), i,
                           qdev_get_gpio_in(sms->gic, irq + 1));
        gpex_set_irq_num(GPEX_HOST(dev), i, irq + i);
    }

    pci = PCI_HOST_BRIDGE(dev);
    if (pci->bus) {
        for (i = 0; i < nb_nics; i++) {
            NICInfo *nd = &nd_table[i];

            if (!nd->model) {
                nd->model = g_strdup("e1000e");
            }

            pci_nic_init_nofail(nd, pci->bus, nd->model, NULL);
        }
    }

    pci_create_simple(pci->bus, -1, "VGA");

    create_smmu(sms, pci->bus);
}
