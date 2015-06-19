#include <stdio.h>

int main(void)
{
    int a = 0x01020304;
    char *c = (char *)(&a);

    /* little endian:  c = [0x4]  */
    /* big endian:  c = [0x1]  */
    printf("c = [0x%x]\n", *c);

    return 0;
}


