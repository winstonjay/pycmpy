.global _start
_start:
	LDR R0, =string_const_0x0000
	MOV R1, #14
	BL io_print

	LDR R0, =string_const_0x0001
	MOV R1, #55
	BL io_print

	MOV R0, #0
	MOV R7, #1
	SWI 0

string_const_0x0000: .asciz "hello, world!\n"
string_const_0x0001: .asciz "...all this work and all I got was this lousy message.\n"

.extern io_print
