/*
#### Multiplication via Bit shifting etc.

`LSL`: logical shift left same as <<
so 15 << 1 = 30
because shifting 01111 one bit left gives 11110.
this is the same as 15 * 2

`LSR`: logical shift right (15 >> 1)
15 >> 1 = 7 

both the same as in other programign languages.
*/
.global _start

_start:
    mov r1, #0xf            @ 15 1111
    mov r0, r1, lsr #0x1    @ shift the value in r1 by 1 bit
                            @ save in register 0.
end:
    mov r7, #0x1
    swi 0

