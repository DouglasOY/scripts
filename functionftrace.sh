root@centos7:/home/cloud/ftrace/fork# cat functionftrace.sh 
#!/bin/bash

debugfs=/sys/kernel/debug
echo nop > ${debugfs}/tracing/current_tracer
echo 0 > ${debugfs}/tracing/tracing_on
echo `pidof haha.elf ` > ${debugfs}/tracing/set_ftrace_pid
echo function_graph > ${debugfs}/tracing/current_tracer
echo do_fork > ${debugfs}/tracing/set_graph_function
echo 1 > ${debugfs}/tracing/tracing_on

root@centos7:/home/cloud/ftrace/fork# cat fork.c 
#include <unistd.h>
#include <stdio.h> 
#include <fcntl.h>

int main (void) 
{ 
    pid_t fpid;
    int count=0;

    sleep(30);
    fpid=fork(); 
    if (fpid < 0) { 
        printf("error in fork!"); 
    }
    else if (fpid == 0) {
        printf("i am the child process, my process id is %d\n",getpid()); 
        count++;
    }
    else {
        printf("i am the parent process, my process id is %d\n",getpid()); 
        count++;
    }
    printf("result: %d\n",count);
    return 0;
}

root@centos7:/home/cloud/ftrace/fork# cat makefile 
haha.elf: fork.o
	gcc -o $@ $^

fork.o : fork.c
	gcc -o $@ -c $^

clean:
	rm *.elf *.o
