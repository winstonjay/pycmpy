/* prog will exit with 2 in r0
    access with ./name ; echo $?
*/
.global _start
_start:
    mov r0, #two

end:
    mov r7, #1
    swi 0

.data
@ equate the word two to the number 2
.equ two, 2
