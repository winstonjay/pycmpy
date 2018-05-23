/*  func2.s loading and unloading 
    multiple values to the stack.
*/
.global _start

@ program should give final result of 32:
@ to run: ./func ; echo $?

_start:
    mov r4, #0xa
    mov r5, #0xe

    stmdb sp!, {R4, R5} @ put multiple val on the stack
    mov r4, #0x3
    mov r5, #0x5
    add r0, r4, r5      @ add into r0 new r1, r2 (3, 5)

    ldmia sp!, {r4, r5} @ get values back off the stack
    add r0, r0, r4      @ add into r0 old r4 10
    add r0, r0, r5      @ add into r0 old r5 14

end:
    mov r7, #1
    swi 0
