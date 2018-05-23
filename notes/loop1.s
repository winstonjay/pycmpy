.global _start 
/*
implement loops like

r0 = 0
r1 = 1
while r0 < 10:
    r0 += r1
*/

_start:
    mov r0, #0x0	/* Move 0 into r0 */
    mov r1, #0x1	/* Move 1 into r1 */
    b _continue_loop	/* Branch to loop */
	
_loop:
    add r0, r0, r1	/* Add 1 to r0 */
_continue_loop:
    cmp r0, #0x9	/* check if r0 isnt greater than 9 */
    ble _loop		/* brach if cmp output is less than equal */
             
end:
    mov r7, #0x1	/* exit */
    swi 0
