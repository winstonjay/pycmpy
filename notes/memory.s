/* 
######## Memory storage

-   Set 2 4 bit varibles as `words` in our 
    memory for use later.
-   
*/

.data
.balign 4           @ set we want to align 4 bits
fifteen:            @ name of varible
    .word 15        @ set the type and value of the varible.
.balign 4           @ repeat again with differnt values.
thirty:
    .word 0         @ Set value to 0 for now and we will set it later.

.text
.global _start

_start:
    ldr r1, addr_fifteen    @ Load address to register.
    ldr r1, [r1]            @ Load the data using its address
    ldr r2, addr_thirty     @ Load address of thirty to r2
    mov r3, #0x1e           @ Store 15 in r3 for use later
    str r3, [r2]            @ Store r3 value inside address stored in r2 `addr_thrity`
    ldr r2, [r2]            @ Load value from address stored in r2
    add r0, r1, r2          @ Into r0 add r1 and r2

end:
    mov r7, #1
    swi 0

addr_fifteen:  .word fifteen
addr_thirty:   .word thirty
