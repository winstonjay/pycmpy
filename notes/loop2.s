.global _start 
/*
implement loops like

r0 = 50
r1 = 2
while r0 >= 2:
    r0 -= 2

*/

_start:
    mov r0, #0x32	/* Move 50 into r0 */
    mov r1, #0x02	/* Move 2 into r1 */
    b _loop		/* Branch to loop */

_decrement:
    subgt r0, r0, r1	@ subtract if greater than 2

_loop:
    cmp r0, r1
    bne _decrement

             
end:
    mov r7, #0x1	/* exit */
    swi 0
