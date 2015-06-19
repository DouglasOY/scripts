#include <stdio.h>

union endian
{
    int i;
    char c[4];
};

int main(void)
{
    int a = 0x01020304;
    char *c = (char *)(&a);

    /* little endian:  c = [0x4]  */
    /* big endian:  c = [0x1]  */
    printf("c = [0x%x]\n", *c);

    union endian data;
    data.i = 0x05060708;
 
    /* little endian: c[0] = [8] */   
    /* big endian: c[0] = [5] */   
    printf("c[0] = [%d]\n", data.c[0]);

    return 0;
}


