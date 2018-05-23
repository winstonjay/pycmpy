/*
(write 123)
*/

.data
.balign 4
buffer: .asciz "_________\n"

.text

.global _start
_start:
    mov r3, #0x0
    @ setup print
    
    mov r2, #1      @ number of chars
    mov r1, #49
    b _continue_loop

_loop:

    @ call to print
    mov r7, #4
    mov r0, #1
    swi 0
    add r3, r3, #0x1

_continue_loop:
    cmp r3, #0x3
    blt _loop    

end:
    mov r7, #1
    swi 0
