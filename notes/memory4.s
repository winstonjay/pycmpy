/*
Memory part 4
    if i wanted to get the value stored at the address i would do.
    ldr r0, [r3]
    we could do
    ldr r0, [r3, #0x4]  @ the 4 is the bit length because we are storing words here.
*/
@ make a list of data called primes
.data
primes:
    .word 2
    .word 3
    .word 5
    .word 7

.text
.global _start
_start:
    ldr r3, =primes     @ load address of info into r3
    ldr r0, [r3, #0x8]

end:
    mov r7, #0x01
    swi 0

