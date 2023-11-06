#include <stdio.h>

main()
{
    int count, loop;
    count = 1;
    loop = count++;
    loop = ++count;
    //count=count+1; loop=count;
    printf("loop = %d, count = %d\n", loop, count);
    loop = count++;
    printf("loop = %d, count = %d\n", loop, count);
    return 0;
}       