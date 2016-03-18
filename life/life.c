
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int lottery = 0;
    int total = 0;
    int sum = 0;
    int count = 0;

    /* head -500000 /dev/urandom > p5000 */
    FILE *fp = fopen("p5000", "rb");
    if (fp == NULL)
    {
        perror("Failed to open file \n");
        return EXIT_FAILURE;
    }

    while (1)
    {
        lottery = fgetc(fp);
        if (lottery == EOF)
        {
            printf("EOF\n");
            break;
        }

        total += 1;
        count += 1;
        if (total < 30000)
        {
            /* 10 --> stardard deviation = 50 */
            if (lottery <= 10) sum -= 1;
            if (lottery >= 245) sum += 1;
        }
        else
        {
            printf("%d\n", sum);
            sum = 0;
            if (lottery <= 10) sum = -1;
            if (lottery >= 245) sum = 1;
            total = 1;
        }
    }

    fclose(fp);
    printf("count = [%d]\n", count);

    return EXIT_SUCCESS;
}


