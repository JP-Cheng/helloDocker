obj = hello.o include.o
hello.out: $(obj)
	g++ -o hello.out $(obj)
hello.o: hello.cpp
	g++ -g -Wall -std=c++17 -c hello.cpp
include.o: include.cpp include.h
	g++ -g -Wall -std=c++17 -c include.cpp

.PHONY: clean
clean:
	rm -rf $(obj) hello.out
