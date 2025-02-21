#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("Hello, os\n");
    printf("My PID is %d\n", getpid());


    return 0;
}