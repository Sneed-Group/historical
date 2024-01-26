SECTION .multiboot
ALIGN 4
extern kern
mboot:
    mov ax, 9ch
    mov ss, ax ;cannot be written directly
    mov sp, 4094d
    mov ax, 7c0h
    mov ds, ax ;cannot be written directly
    call kern
quit:
    hlt
    jmp quit
    jmp $
    times 510-($-$$) db 0
    dw 0xAA55