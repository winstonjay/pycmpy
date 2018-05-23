/*
hello world

using io package with io_wite function
to print asciz strings.
*/
    .global _start
    .extern io_write
    .extern io_read

_start:
    
    ldr r0, =const      @ load string
    mov r1, #12         @ load string len
    bl io_write
    
    ldr r0, =num
    mov r1, #2
    bl io_read
    
    mov r1, #2
    ldr r0, =num
    bl io_write
    
    mov r1, #0 
/* 
    ldr r0, =num
    mov r1, #5
    bl io_write
*/
_end: 
    mov r0, #0
    mov r7, #1
    swi 0

.data
num: .asciz "  "
const: .asciz "write num: "
