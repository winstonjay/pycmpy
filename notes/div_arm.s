/*
div_armv.s:

Provide routines performing division, because apparently
the raspberry pi `as` compiler dosent have any.
*/

.global udivide
.global sdivide
.global divide_10


udivide:
    push    {r4-r12, lr}

    @ ####################### TODO

    pop     {r4-r12, lr}
    bx      lr


sdivide:
    push    {r4-r12, lr}

    @ ####################### TODO

    pop     {r4-r12, lr}
    bx      lr


divide_10:
    push    {r4-r12, lr}

    @ ####################### TODO

    pop     {r4-r12, lr}
    bx      lr