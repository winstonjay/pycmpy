/*
Memory part 5
we are using bytes now instead
of words and to incrment through 
elements of a list move in single digits.
*/

.text
.global _start
_start:
    ldr r3, =numbers   @ load address of info into r3
    ldr r0, [r3, #2]   @ load item at second index of our list.         

end:
    mov r7, #0x01
    swi 0

.data
numbers:
    .byte 1, 2, 3, 4, 5
