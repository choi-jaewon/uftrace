/*
 * This is test to trace function in a library.
 */
#include <unistd.h>

int lib_a(int i);
int lib_b(int i);
int lib_c(int i);

int lib_a(int i)
{
	return lib_b(i + 1) - 1;
}

int lib_b(int i)
{
	return lib_c(i - 1) + 1;
}

int lib_c(int mask)
{
	return getpid() % mask;
}

