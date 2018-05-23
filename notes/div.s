

.global _start
/*
divide 2 32 bit ints
args:   r1 = divdend
        r2 = divisor

returns:
        r3 = quotient
        r2 = original divisior
        r1 = remainder
*/
_start:
    mov     r1, #12         @ 12 / 3 = 4
    mov     r2, #3 
    mov     r4, r2          @ put divisor in r4
    cmp     r4, r1, lsr #1  @ double until 2 x r4 > divisor
    
div1:
    movls   r4, r4, lsl #1
    cmp     r4, r1, lsr #1
    bls     div1
    mov     r3, #0          @ init quotient

div2:
    cmp     r1, r4          @ can we subtract r4
    subcs   r1, r1, r4      @ if we can do so
    adc     r3, r3, r3      @ double quotient & add a new bit
    mov     r4, r4, lsr #1  @ halve r4
    cmp     r4, r2
    bhs     div2            @ loop til we gone past the og divisor

_write:
    mov     r1, r3          @ move r1 out the way
    ldr     r1, =digit
    add     r3, #48         @ add '0' to make num ascii
    str     r3, [r1]        @ str r3 (quotient) in addr in r1
    mov     r2, #1          @ len of string
    mov     r0, #1          @ stdout
    mov     r7, #4          @ syscall write
    swi     0               @ make print call
    
    mov r3, #10             @ '\n'
    str r3, [r1]
    swi 0
    
    mov r0, r3
    mov r7, #1
    swi 0


.data
digit:      .ascii " "
