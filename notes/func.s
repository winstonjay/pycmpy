.data

.balign 4
lr_bu:   .word 0

.balign 4
message: .asciz "hello world\n"


.text

/* print to the screen an input from
   regisister 1.
*/
io_print:
    ldr r2, addr_lr_bu  @ set link reg backup
    str lr, [r2]            
    stmfd sp!, {r4-r12} @ store these on stack as we
                        @ will change them in this func.
    
    mov r7, #4          @ sys call to ouput
    mov r0, #1          @ monitor output to screen
    mov r2, #13         @ max string length
                        @ input should be set in r1 before calling
    swi 0
    
    ldmfd sp!, {r4-r12} @ get vals back from stack.
    ldr lr, addr_lr_bu  @ restore the link reg
    ldr lr, [lr]
    bx lr
    
    


.global _start
_start:
    
    ldr r1, =message   @ load register with address of str
    bl io_print        @ call function 


end:
    mov r7, #1
    swi 0


addr_lr_bu: .word lr_bu
