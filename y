
MOV AX, 0x07C0          ; Set up stack segment for Bootloader
MOV DS, AX
MOV SI, msg             ; Load our artistic message
print_loop:
    LODSB
    OR AL, AL
    JZ stop
    INT 0x10            ; BIOS Video Interrupt to print characters
    JMP print_loop
stop:
    CLI                 ; Halt the system into the song loop
    HLT
msg db 'LOADING CRAZY DATA SYSTEM...', 0


