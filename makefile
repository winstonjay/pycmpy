$(fn): $(fn).o io.o
	ld -o $(fn) $(fn).o io.o
$(fn).o: $(fn).s lib/io.s
	as -o $(fn).o $(fn).s
	as -o io.o lib/io.s
clean:
	rm *.s
	rm *.o
debug:
	as -g -o outfile.o outfile.s
	ld -o outfile outfile.o
	gdb outfile
gcc:
	gcc -o outfile outfile.s

