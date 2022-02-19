#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> /* For sleep and fork warning */
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
	int pid = 0;

	while (process < 5) /* Creates 5 zombie processes */
	{
		pid = fork(); /* Create a child process */
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
