#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int lottery = 0;
    int total = 0;
    int positive = 0;
    int negative = 0;

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
        if (lottery == EOF) break;

        total += 1;
        if (lottery <= 10) negative -= 1;
        if (lottery >= 245) positive += 1;

        if (total == 30000)
        {
            /*printf("%d    %d    %d    %d\n", positive, negative, (positive + negative), (positive - negative));*/
            printf("%d    %d\n", positive, negative);
            positive = 0;
            negative = 0;
            total = 0;
        }
    }

    fclose(fp);

    return EXIT_SUCCESS;
}

