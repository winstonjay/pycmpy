.global _start

_start:
    MOV R1, #0x14 	@ load 20 into R1
    MOV R2, #0x64       @ load 100 into R2
    ADD R0, R1, #0xC0   @ add 192 to R1 into R0
    SUB R0, R0, R2      @ sub 200 from R0
    MOV R7, #1		@ exit with 112 in R0
    SWI 0






