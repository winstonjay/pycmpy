# -*- coding: utf-8 -*-
'''
Module compiles a basic instructions from a C like language
into ARM ASM for raspberry pi.

The specification to the language is given as follows:

    start -> list EOF

    list -> stmt ; list | €

    stmt -> expr
        | print expr

    expr -> expr + term         { print('+') }
        | expr - term           { print('-') }
        | term

    term -> term * factor       { print('*') }
        | term / factor         { print('/') }
        | factor

    factor -> ( expr )
        | id                    { print(id.lexeme) }
        | num                   { print(num.value) }

some of this is incorect or out dated.
See individual components for futher implementation details.

TODO:
- implement read ops, parsing and std library function.
- work out a way of printing numbers without using printf and gcc
- implement conditional statements (this shouldnt be too hard right).
- implement varible assignments. (most basic would be like how string
    constants are currently defined.
- find a better way to compile and link asm, atm the makefile wont work
    unless the output is named 'outfile.s'

'''
from __future__ import print_function
import os
import argparse
import subprocess

from pycmpy.scanner import Scanner
from pycmpy.parser import Parser
from pycmpy.emitter import Emitter

def main():
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="source file to compile",
        type=str)
    parser.add_argument(
        "-o",
        "--out",
        help="output filename",
        type=str)
    parser.add_argument(
        "-p",
        "--pause",
        help="pause before linking and just print .s file to screen",
        action="store_true")
    args = parser.parse_args()

    # read source file or return an error
    try:
        with open(args.file, "r") as fp:
            source = fp.read()
    except IOError:
        print("Error, file not found:", args.file)
        return

    parser = Parser(Scanner(source))
    stack = parser.parse()
    if not any(stack):
        return

    if args.pause or 'raspberrypi' not in os.uname():
        printer = Emitter(stack, out=None)
        printer.emit()
        return
    print("got here")
    return
    # compile then assemble.
    printer = Emitter(stack, out=args.out)
    printer.emit()
    print("Created file: %s.s" % args.out)
    print("making executable...\n%s" %  ("-"*48))
    try:
        # just do this for now in the future
        # sort out how to do this better with
        # the right dependency files linked in only.
        subprocess.check_call(["make", "fn=%s" % args.out])
        print("-"*48,
              "\nsuccessfully created executable:'%s'"
              "\nto run: $ ./%s" % (args.out, args.out))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
