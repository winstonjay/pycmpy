/*
######## Text to uppercase.

Given the binary representation of a letter such as...
    a : 0110 0001
    A : 0100 0001

We can see that there is only one bit difference between
the two. Becuase of this we can use BIC (bit clear method)
to change a lower case letter to an upper case.

BIC Rn, 0x61, 0x20 gives us 0x41
changing in this example lowercase a to uppercase A.
a:  0110 0001   0x61    97
    0010 0000   0x20    32
A:  0100 0001   0x41    65
   
*/
.global _start

_start:
    MOV R7, #0x3        @ syscall keyboard 3 in R7
    MOV R0, #0x0        @ Input stream Keyboard
    MOV R2, #0x1        @ Read 1 char
    LDR R1, =char
    SWI 0

_uppercase:
    LDR R1, =char
    LDR R0, [R1]
    BIC R0, R0, #0x20   @ change input char to uppercase
    STR R0, [R1]

_write:
    MOV R7, #0x4        @ syscall output to screen
    MOV R0, #0x1        @ Output as our monitor
    MOV R2, #0x1        @ set number of chars to 1
    LDR R1, =char
    SWI 0
 
end:
    MOV R7, #0x1
    SWI 0

.data
char:
    .ascii " "
