#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main(void) 
{ 
    int fd;
    char buf[4096];

    printf("pid = [%d]\n", getpid()); 
    sleep(10);

    fd = open("/home/annabel/orig/README", O_RDONLY);
    read(fd, buf, 4096);
    read(fd, buf, 4096); 
    return 0; 
}

