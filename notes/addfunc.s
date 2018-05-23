/*  using functions to structure our code.
    (def custom functions here). we can pass
    and stor args in the registers 1..3, if 
    we want pass more we need to store the values
    in the stack, and then pull them off the stack
    inside of the function. we can modif other
    registers insde of our functions but we should 
    return these to their intial state when we are
    done. to set the values back you can do the 
    following:
    
    before/ start of function:
        stmfd sp!, {r4-r12}
        
    when we leave
        ldmfd sp!, {r4-r12}

    probally dont change sp that is register 13.
    allways store the link resgister before you start
    a function and return it when you are done.

    when ever you return a function it is going to return
    the value in register 0 always.
*/

@ PROG GOAL: user enter 2 vals, sum and return result.

@ start off by defining some data
@ all the different varibles we will need.

.data

@ def our strings
.balign 4
get_val_1: .asciz "a = "
.balign 4
get_val_2: .asciz "b = "
.balign 4
pattern:   .asciz "%d"
.balign 4
output:    .asciz "%d + %d = %d\n"

@ def our numbers
.balign 4
num_a: .word 0
.balign 4
num_b: .word 0
.balign 4
sum:   .word 0

@ def our link registers that we will 
@ back up twice in our functions.
.balign 4
lr_bu_1: .word 0
.balign 4
lr_bu_2: .word 0


.text

@ def our custom function
sum_vals:
    ldr r2, addr_lr_bu_2    @ store link reg in r2
    str lr, [r2]
    
    add r0, r0, r1          @ sum values passed to r0, r1
    
    ldr lr, addr_lr_bu_2    @ restore link register
    ldr lr, [lr]
    bx lr                   @ exit function like this
                            @ (pass back link register)

addr_lr_bu_2: .word lr_bu_2

@ we aint using '_start' so we have to define 
@ main for the c library.

.global main

main:
    @ allways store link register back up for function.
    ldr r1, addr_lr_bu_1
    str lr, [r1]
    
    @ load addr to register
    ldr r0, addr_get_val_1
    bl printf
    
    @ load first two args for scanf     
    ldr r0, addr_pattern
    ldr r1, addr_num_a
    bl scanf
    
    @ do the same again for second value
    
    ldr r0, addr_get_val_2
    bl printf
    
    ldr r0, addr_pattern
    ldr r1, addr_num_b
    bl scanf
    
    @ load values from addrs run our custom function.
    ldr r0, addr_num_a
    ldr r0, [r0]
    ldr r1, addr_num_b
    ldr r1, [r1]
    bl sum_vals
    
    @ get return value of function store in r3 for printf
    mov r3, r0
    
    @ load the rest of the vals for printf.    
    ldr r0, addr_output     @ pass output str as ref? 
    ldr r1, addr_num_a
    ldr r1, [r1]
    ldr r2, addr_num_b
    ldr r2, [r2]
    bl printf

    @ finally restore the link register.
    
    ldr lr, addr_lr_bu_1
    ldr lr, [lr]
    bx lr
    

@ define our addresses for our data

addr_get_val_1: .word get_val_1
addr_get_val_2: .word get_val_2
addr_pattern:   .word pattern
addr_output:    .word output
addr_num_a:     .word num_a
addr_num_b:     .word num_b
addr_sum:       .word sum
addr_lr_bu_1:   .word lr_bu_1

.global printf
.global scanf













