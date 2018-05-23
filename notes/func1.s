/*
    functions, directives, etc.
    stacks - last in first out
*/

.global _start

_start:
    mov r1, #0xa        @ move values into r1 and r2
    mov r2, #0xb        
    str r1, [sp, #-4]!  @ sp = stack pointer decrement by -4
                        @ '!' is known as the rightback.
                        @ it updates so we can put another 
                        @ register inside the stack.
    str r2, [sp, #-4]!  @ same again.
    
    ldr r0, [sp], #+4   @ pop value off of the stack
    ldr r0, [sp], #+4   @ pop next value off the stack

end:
    mov r7, #1
    swi 0

