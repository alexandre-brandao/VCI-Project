.PHONY: run clean cleanall doc help

CC=gcc

CFLAGS=-Wall

tester : heatingsystem.o heatingSM.o tester.o
	gcc -o tester $^

run : tester
	./tester

clean :
	rm -f *.o *~
	rm tester

help :
	@echo "make [arg ]"
	@echo "where optional arg is:"
	@echo "run      : run target code"
	@echo "clean    : delete object files"
