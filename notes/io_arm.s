/*
io_arm.s:

Provide routines for input and output.

#### USE
See notes per function for use parameters.

## Reading and writing (prog how to notes).

Both reading and writing can be done with systems calls.
To do this we use the "SoftWare Interupt" instruction
`SWI` with our registers set to the following parameters:

system read:
    R0 = input stream (stdin); R0 = 0
    R1 = buffer address to read into.
    R2 = number of characters to read.
    R7 = system call number; R7 = 3

system write:
    R0 = output stream (stdout); R0 = 1
    R1 = output string address
    R2 = output string length
    R7 = system call number; R7 = 4
*/
.global io_read
.global io_write

/*
params:
    r0 = <string addr>
    r1 = <string len>
print a string ended with a newline token.
*/
io_read:
    push    {r4-r12, lr}        @ backup reg 4-12 and link register on stack
    mov     r2, r1              @ re-order user args for call to read
    mov     r1, r0
    mov     r7, #sys_read        @ setup sys args for call to read
    mov     r0, #stdin
    swi     0                   @ sys call.
    pop     {r4-r12, lr}        @ get vals back from stack
    bx      lr                  @ exit function

/*
params:
    r0 = <string addr>
    r1 = <string len>
*/
io_write:
    push    {r4-r12, lr}        @ backup reg 4-12 and link register on stack
    mov     r2, r1              @ re-order user args for call to write
    mov     r1, r0
    mov     r7, #sys_write      @ setup sys args for call to write
    mov     r0, #stdout
    swi     0                   @ sys call.
    pop     {r4-r12, lr}        @ pop backups of the stack
    bx      lr                  @ exit function


.equ sys_read,  3   @ raspian system calls
.equ sys_write, 4

.equ stdin,  0      @ system locations
.equ stdout, 1


