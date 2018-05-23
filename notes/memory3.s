/*
Memory part 2
*/
.data
.balign 4
info: 
    .word 10

.text
.global _start
_start:
    ldr r3, =info   @ load address of info into r3
    mov r4, #0x64   @ load 100 into r4
    str r4, [r3]    @ get address stored in r4 and store in r3
    ldr r0, [r3]    @ get the value of address by using brackets.
end:
    mov r7, #0x01
    swi 0

