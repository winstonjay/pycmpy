/*
switch statements.
*/

.global main
.func main
main:
    mov r2, #1
    cmp r2, #0
    beq case_0
    cmp r2, #1
    beq case_1    
    b case_def

case_0:
    ldr r0, =out_0
    b end
case_1:
    ldr r0, =out_1
    b end
case_def:
    ldr r0, =out_def

end:
    bl puts
    mov r7, #1
    swi 0

.data
out_0:   .asciz "it 0"
out_1:   .asciz "it 1"
out_def: .asciz "i dont know"

.global puts
