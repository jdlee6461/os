/*
 * Solution to question 3.1
 * 
 * Answer is 5 as the child and parent processes
 * each have their own copy of value.
 */

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int value = 5;

int main()
{
	pid_t pid;

	pid = fork();
	
	if (pid == 0) { /* child process */
		value += 15;
		printf ("CHILD (%d): value = %d\n", getpid(), value); /* LINE A */
		return 0;
	}
	else if (pid > 0) { /* parent process */
		wait(NULL);
		printf ("PARENT (%d): value = %d\n", getpid(), value); /* LINE A */
		sleep(10);
		return 0;
	}
}
