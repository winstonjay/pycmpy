/*
######## Conditional Ops
Where a = 5, b = 9:
    AND = a & b = 1
    ORR = a | b = 13
    EOR = a ^ b = 12
    BIC   a,b   = 4

# BIC = Bit clear?
   
*/
.global _start

_start:
    MOV R1, #0x5        @ mov 5 into r1 (0101)
    MOV R2, #0x9        @ mov 9 into r2 (1001)
    BIC R0, R1, R2
end:
    MOV R7, #0x1
    SWI 0

