/*
(let foo (* 16 (+ 4 3 1)))
*/

.data


.balign 4
foo: .word 5            @ init value

.text



.global _start
_start:   
    mov r1, #0x4
    add r1, #0x3
    add r1, #0x1
    mov r0, #0x10
    mul r1, r0
    ldr r2, =foo
    str r1, [r2]
    ldr r0, [r2]

end:
    mov r7, #1
    swi 0

