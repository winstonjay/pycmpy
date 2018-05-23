/*
io.s:
provide routines for input and output.
*/
.data
.balign 4
    lr_bu: .word 0

.text

.global io_print
/*
print function for strings.

USE:
load string addr into R0 and string lenght into R1
then call with bl.

Currently supported types: 
    .asciz

TODO: 
work out how to print numbers and other forms
of formating goal is to mimic printf but without
using C or anything.
*/
io_print:
    stmfd sp!, {r4-r12} @ backup reg 4 to 12 on stack
    ldr r2, addr_lr_bu  @ set link reg backup
    str lr, [r2]
    
    mov r2, r1      @ re-order args for print call
    mov r1, r0      @ len in r2, string in r1

    mov r7, #4      @ make sys call to print
    mov r0, #1
    swi 0
    
    ldmfd sp!, {r4-r12}  @ get vals back from stack
    ldr lr, addr_lr_bu   @ restor link reg
    ldr lr, [lr]
    bx lr

addr_lr_bu: .word lr_bu


