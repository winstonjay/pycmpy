@ Hello asm i am a comment
.global _start

_start:
    MOV R7, #3 		@ syscall read from keyboard 
    MOV R0, #1		@ input stream keyboard
    MOV R2, #10		@ read 10 chars
    LDR R1, =message	@ put string in message
    SWI 0

_write:
    MOV R7, #4 		@ syscall to outpt to screen
    MOV R0, #1 		@ Output to monitor
    MOV R2, #5		@ number of chars to write
    LDR R1, =message 	@ print message to screen
    SWI 0

end:
    MOV R7, #1
    SWI 0

.data
message:
   .ascii "\n"


