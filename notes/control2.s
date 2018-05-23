.global _start 

_start:
    MOV R1, #0x9    @ 9 1001
    MOV R2, #0x8    @ 8 1000
    TST R1, R2
    BEQ _bit_set
    MOV R0, #0x1
    B   end    

_bit_set:
    MOV R0, #0x0

end:
    MOV R7, #0x1
    SWI 0
