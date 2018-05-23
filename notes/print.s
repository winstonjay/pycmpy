/*
print binary numbers...
*/

.global _start

_start:
    mov r6,  #251           @ number to print
    mov r10, #1             @ set up mask
    mov r9, r10, lsl #31    @ left shift 32 bits.
    ldr r1, =string         @ point r1 to string
    
_bits:
    tst r6, r9              @ tst num, mask
    moveq r0, #48           @ ascii '1'
    movne r0, #49           @ ascii '0'
    str r0, [r1]            @ store result of r0  in string
    bl _write               @ write to screen
    movs r9, r9, lsr #1
    bne _bits

_exit:
    mov r0, #10             @ ascii '\n'
    str r0, [r1]
    bl _write
    mov r0, #0
    mov r7, #1
    swi 0

_write:
    push    {r4-r12, lr}        @ get vals back from stack
    mov r0, #1
    mov r2, #1
    mov r7, #4
    swi 0
    pop     {r4-r12, lr}        @ get vals back from stack
    bx      lr                  @ exit function



.data
string: .ascii " "
    

    



