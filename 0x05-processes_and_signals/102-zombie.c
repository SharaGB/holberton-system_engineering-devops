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
	int i = 0, process_id;

	while (i < 5)
	{
		process_id = fork();
		if (process_id > 0)
			printf("Zombie process created, PID: %d\n", process_id);
		else
			return (0);
		i++;
	}
	infinite_while();
	return (0);
}
