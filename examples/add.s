.global _start
_start:
	MOV R0, #10
	MOV R1, #10
	MOV R2, #2
	MUL R1, R2
	ADD R0, R1

	MOV R0, #0
	MOV R7, #1
	SWI 0

.extern io_print
