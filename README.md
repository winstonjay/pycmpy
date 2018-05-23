# pycmpy

Learning about compilers and the assembly language with the Raspberry Pi.

Most files are mainly just examples, some may not work.

[`pycmpy/`](pycmpy/) folder contains a semi functional compiler written in python. It can add numbers and stuff, just not print them. It can print words, just not do anything else with them. See the directories README for more info.


### pycmpy compiler

We can compile super non-trivial programs like this that will totally blow your mind. Say we have source file `hello.cmpy` whose contents is as follows:

```perl
print "hello, world!";
```
We can use `pycmpy` to compile this to native machine code by runninging (from within this directory):

```bash
$ python pycm.py hello.cmpy -o hello
```


What this will do is take the file `hello.cmpy` and create the executable `hello`. You should see an output like this.

```
Created file: hello.s
making executable...
------------------------------------------------
as -o hello.o hello.s
as -o io.o lib/io.s
ld -o hello hello.o io.o
Created file: hello.s
------------------------------------------------
successfully created executable:'hello'
to run: $ ./hello
```

We can now run this crazy program.

```bash
$ ./hello
hello, world!
```

Behind the scenes `pycmpy` created the file `hello.s` which in this case looks like this.

```asm
.global _start
_start:
	LDR R0, =string_const_0x0000
	MOV R1, #14
	BL io_print

	MOV R0, #0
	MOV R7, #1
	SWI 0

string_const_0x0000: .asciz "hello, world!\n"

.extern io_print
```

The io_print routines and possibly others are defined in the `lib` directory. After creating this it hands the rest over to `as` and `ld` who finish the job creating the executable.