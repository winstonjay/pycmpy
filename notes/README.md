# Notes

Directory contains lots of half done half working examples.

**Assembling files** (assuming src = `add.s`)

    $ as -o add.o add.s
    $ ld -o add add.o

**echoing R0** (value stored in register 0 at the end of the program).

    $ ./add ; echo $?


**Debugging**

to compile for debugging add the following flag.

```
$ as -g -o <file.o> <file.s>
$ ld -o <file> <file.o>
```

once this has been compiled we can use the program in `gdb`

To start `gdb` run:
	$ gdb <file>

```
(gdb) disassemble _start    <- disassemble code in start section.
(gdb) b 20 				    <- set breakpoint at line 20
(gdb) delete				<- delete all breakpoints
(gdb) run		            <- run program if breakpoint it will stop at that point.
(gdb) info r		        <- show info stored in our registers
(gdb) continue		        <- run till the next breakpoint
```

you can use continue etc untill the program finishes running then you can start again

```
(gdb) quit 		<- exit gdb
```

I have added a debugging option on our makefile to make it easier to debug.


http://www-mdp.eng.cam.ac.uk/web/library/enginfo/mdp_micro/lecture3/lecture3-3-3.html