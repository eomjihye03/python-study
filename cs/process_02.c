#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("parent PID is %d\n", getpid());

    if (fork() == 0) {
        printf("child PID is %d\n", getpid());
    }

    printf("executed!!!\n");
    return 0;
}

// fork가 된 순간 동일한 코드를 실행하는 자식 프로세스가 생성되었다