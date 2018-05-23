'''
The Emitter takes a post-fix ordered stack, finished the translation
to the raspi ARM instruction set and prints out the result to a
given file.

## general strategy at the moment:
forget about being optimal for now. keep commands simple as possible.

operations:
increment throught the parsed stack one by one; when a number is found
print the comand to move it into the lowest availble register, then
increment the reg index. when a opperator is found add the highest 2
registers and decrement the register index. If we reach the end of a
statement reset the regisiter index back to 0.

eg input: `print 1 + 2 * 3`

eg as post-fix: `1 2 3 * + print`

eg outputs:`
    MOV R0, #1
    MOV R1, #2
    MOV R2, #3
    MUL R1, R2
    ADD R0, R1
    print
`
(print function is defined externally)
(also we cant actuall print numbers yet lole)
'''
from __future__ import print_function
import sys

import token

class Emitter(object):
    '''
    Emitter prints the translated code. it takes a pre parsed stack
    and pieces together what it needs to make a compilable asm file.
    '''
    def __init__(self, stack, out="outfile"):
        self.stack = stack
        self.out = out

    def emit(self):
        "print to file the parsed program."
        ptr, reg = 0, 0
        curr = self.stack[ptr]
        data = []
        outfile = open("%s.s" % self.out, "w") if self.out is not None else sys.stdout

        def fprintf(fmt, *args):
            print(fmt.format(*args), file=outfile)

        fprintf(".global _start\n_start:") # start of program.
        while curr.name != token.EOF:
            if curr.name == token.INT:
                fprintf("\tMOV R{}, #{}", reg, curr.literal)
                reg += 1
            elif curr.name == token.STRING:
                data.append(("asciz",
                             "string_const_{:#0{}x}".format(len(data), 6),
                             curr.literal))
                fprintf("\tLDR R{}, ={}", reg, data[-1][1])
                reg += 1
                fprintf("\tMOV R{}, #{}", reg, len(data[-1][2])+1)
                reg += 1
            elif curr.name in token.op_names:
                reg -= 1
                fprintf("\t{} R{}, R{}", curr.name.upper(), reg-1, reg)
            elif curr.name == token.SEMI:
                reg = 0
                fprintf("") # just for now debuggin and to split up statements.
            elif curr.name in token.keywords:
                # print(last)
                fprintf("\tBL io_{}", curr.name)
            last = curr.name
            ptr += 1 # allways increment the pointer.
            curr = self.stack[ptr]

        fprintf("\tMOV R0, #0") # exit status 0. (success)
        fprintf("\tMOV R7, #1") # move for sys call
        fprintf("\tSWI 0")      # sys call "system interupt"

        if len(data) > 0:     # print any data we need.
            fprintf("")
            for t, name, lit in data:
                fprintf("{}: .{} \"{}\\n\"", name, t, lit)
                # fprintf(".equ {}_len, {}", name, len(lit))
        fprintf("\n.extern io_print")
        outfile.close()
