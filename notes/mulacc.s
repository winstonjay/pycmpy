.global _start

_start:
    MOV R1, #0x14 	@ load 3 into R1
    MOV R2, #0xA        @ load 2 into R2
    MOV R3, #0x5        @ load 5 into R3
    MLA R0, R1, R2, R3  @ mul with acumulate r1, r2, r3 into r1 (3 * 2 * 5)
    MOV R7, #1		@ exit with 30 in R0
    SWI 0






