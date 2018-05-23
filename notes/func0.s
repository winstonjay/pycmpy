
.global _start

_start:
    mov r0, #8
    add r1, r0, #48

    ldr r1, =num
    str r0, [r1]

    mov r0, #1
    ldr r1, =num
    mov r2, #1
    mov r7, #4
    swi 0

end:
    mov r7, #1
    swi 0

.data
num: .ascii " "
