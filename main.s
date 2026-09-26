.global _start

.section .text

_start:
    mov     x0, #1              // stdout
    adr     x1, message         // address of message
    mov     x2, #24             // message length
    mov     x8, #64             // write syscall
    svc     #0

    mov     x0, #0              // exit status
    mov     x8, #93             // exit syscall
    svc     #0

.section .rodata

message:
    .ascii  "Local AI Core started!\n"
