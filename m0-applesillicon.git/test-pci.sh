#!/bin/bash

# NOTE: MAINTAINERS ON PCI SUPPORT WANTED!
# SEE /QEMU-SRC/HW/ARM/(j273_macos11.c+hacky-pci.c) FOR THE CURRENT PCI HACK
# (WHICH DOESN'T WORK, SADLY.)

./xnu-qemu-arm64-5.1.0/aarch64-softmmu/qemu-system-aarch64 \
-M macos11-j273-a12z,\
kernel-filename=kernelcache.release.j273.out,\
dtb-filename=DeviceTree.j273aap.im4p.out,\
ramdisk-filename=arm64eSURamDisk.dmg.out,\
kern-cmd-args="kextlog=0xfff cpus=1 rd=md0 serial=2 -noprogress",\
xnu-ramfb=off \
-cpu max \
-m 6G \
-device virtio-mouse \
-device virtio-keyboard \
-global ICH9-LPC.acpi-pci-hotplug-with-bridge-support=off \
-smbios type=2 \
-device e1000-82545em,netdev=net0,id=net0,mac=52:54:00:0e:0d:20 \
-monitor stdio \
-vga vmware
