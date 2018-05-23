.global _start
/*
Program demonstrates use of 'CMP' to do
comparisons. 

CMP minuses the first by the second and then
we check the Comuter Register status to see if
neg flag is rasied etc with conditional branches.

240 is bigger than 20 so should return 2
*/

_start:
    MOV R1, #0x14 	@ load 20 into R1
    MOV R2, #0xF0       @ load 240 into R2
    CMP R1, R2          @ Compare R1, R2 (R1 - R2) 
    BEQ val_equal       @ branch if R1 == R2
    BGT r1_gt   	@ branch if R1 > R2
    BLT r1_lt		@ branch if R1 < R2

val_equal:
    MOV R0, #0x0
    B	end

r1_gt:
    MOV R0, #0x1
    B   end

r1_lt:
    MOV R0, #0x2
    B   end

end:
    MOV R7, #0x1
    SWI 0





