/*
    floating point stuff
    basically throw a v infront of stuff.
    arith directives:
        vadd, vsub, vdiv, vabs, vsqrt
    we have to use s registers, and double reges.
*/

.global main
.func main
main:
    ldr r1, addr_num_1
    vldr s0, [r1]
    vsqrt.f32 s2, s0        @ sqrt of 25?
    
    vcvt.f64.f32 d1, s2     @ convert to double for printf
    ldr r0, =out_1
    vmov r2, r3, d1
    bl printf
    
    ldr r1, addr_pi
    vldr s0, [r1]           @ store val in s reg
    ldr r2, addr_num_2
    vldr s1, [r2]
    
    vadd.f32 s2, s0, s1     @ single prec float add
    
    vcvt.f64.f32 d1, s2     @ to double for printf 
    ldr r0, =out_2         
    vmov r2, r3, d1
    bl printf
    
end:
    mov r7, #1
    swi 0

addr_pi:    .word pi
addr_num_1: .word num_1
addr_num_2: .word num_2

.data
pi:     .float 3.141592
num_1:  .float 25.0
num_2:  .float 1.2345
out_1:  .asciz "sqrt(25) = %f\n"
out_2:  .asciz "pi + 1.2345  = %f\n"

.global printf
