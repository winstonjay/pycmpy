/* ask the user a question by printing 
   with printf. get response with scanf
   print message with user response using 
   printf again.

    must compile with
    gcc -o func3 func3.s
*/

.data
.balign 4
question: .asciz "what is ya fave number? "

.balign 4
message: .asciz "%d is a great number\n"

.balign 4
pattern: .asciz "%d"

.balign 4
number: .word 0

@ link register backup.
.balign 4
lr_bu: .word 0


.text
.global main
.func main

main:
    /* allways do the next 2 lines first for funcs*/
    ldr r1, addr_lr_bu
    str lr, [r1]
    
    /* allways store function values in register 1 2 or 3 
       if you wanna pass values to functions use these as well.
       if you wanna pass more you wanna use the stack for this. 
       can edit values within the function of registers, stack pointer
       etc, but you wanna return these back to what they were
       before you enterned the function. */
    ldr r0, addr_question   @ load question into r0
    bl printf               @ call printf (branch to it)
    
    /* load the 2 args for scanf to be auto passed */
    ldr r0, addr_pattern    @ load address of pattern
    ldr r1, addr_number     @ load address of number
    bl scanf
    
    ldr r0, addr_message    
    ldr r1, addr_number
    ldr r1, [r1]            @ get value out of the address.
    bl printf

    /* allways return the link register after functions. */
    ldr lr, addr_lr_bu
    ldr lr, [lr]
    bx  lr

addr_question: .word question
addr_message:  .word message
addr_pattern:  .word pattern
addr_number:   .word number
addr_lr_bu:    .word lr_bu

/* load c functions */  
.global printf
.global scanf



