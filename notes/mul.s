.global _start

_start:
    MOV R1, #0x14 	@ load 20 into R1
    MOV R2, #0xA        @ load 10 into R2
    MUL R0, R1, R2      @ mul R1 by R2 into R0
    MOV R7, #1		@ exit with 200 in R0
    SWI 0






