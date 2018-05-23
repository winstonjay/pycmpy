/*
###### stacks
works like all stacks "last in first out"
sp <- stack pointer

basically accessing will be done by increasing
and descreasing stack pointer address.
*/
.global _start

_start:
    mov r1, #1
    mov r2, #2
    str r1, [sp, #-4]!      @ take the value of r1 push onto the stack 
                            @ the `!` is known as the right back allows us to push
                            @ another value onto the stack.
    str r2, [sp, #-4]!      @ once again update our register.
    
    ldr r0, [sp], #+4       @ load value from stack pointer move 4 through memory.
    ldr r0, [sp], #+4       @ same again but now we will be at the top of the stack.

end:
    mov r7, #1
    swi 0

    


