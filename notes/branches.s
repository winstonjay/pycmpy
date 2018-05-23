.global _start
/*
Demonstrates how branching works
program should return 20 + 3 not 11
*/

_start:
    MOV R0, #0x14 	@ load 20 into R0
    B other_branch
    MOV R0, #0xB	@ load 11 into R0 (this shouldnt run)

other_branch:
    ADD R0, R0, #0x3
    MOV R7, #1
    SWI 0






