/*
block transfer list of values into multiple registers.
*/
.text
.global _start
_start:
    adr r3, numbers         @ load numbers into r3
    ldmia r3, {r5-r8}       @ block transfer numbers r5 to r8
    mov r0, r6

end:
    mov r7, #0x01
    swi 0

@ if we put this part in data we get an error. I dont understand why tbh.
.align 2                    @ enforce 2 byte alignment.
numbers:
    .word 1, 2, 3, 4
