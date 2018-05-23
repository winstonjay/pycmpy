/*
(write 123)
*/

.data
.balign 4
buffer: .asciz "_________\n"

.text

.global _start
_start:


    mov r7, #4      @ set for output sys call
    mov r0, #1      @ output as monitor
    mov r2, #10      @ number of chars
    ldr r1, =buffer   @ set output to char
    swi 0
    
   
end:
    mov r7, #1
    swi 0

.data
char:   .ascii "K"
