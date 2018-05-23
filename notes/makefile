func: func.o
	ld -o func func.o
func.o: func.s
	as -o func.o func.s
clean:
	rm *.o
debug:
	as -g -o func.o func.s
	ld -o func func.o
	gdb func
gcc:
	gcc -o func func.s

