#include <stdio.h>
#include <stdlib.h>
/**
 * infinite_while - Infinite loop that pause for 1 second.
 *
 * Return: Void.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Program that creates 5 zombie processes.
 *
 * Return: Void.
 */
int main(void)
{
	int process = 0;
	int pid = fork(); /* Create a child process */

	while (process < 5)
	{
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
		{
			exit(0);
		}
		process++;
	}
	infinite_while();
	return (0);
}
