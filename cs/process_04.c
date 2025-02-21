#include <stdio.h>
#include <unistd.h>

// 식 프로세스는 얼마든지 또 다른 자식 프로세스를 생성할 수도 있고, 부모 프로세스 또한 또다른 자식 프로세스를 생성할 수 있습니다.

void foo() {
    printf("execute foo()!!!\n");
}

int main()
{
    if (fork() == 0) {
        if (fork() == 0) {
            printf("child of child PID is %d\n", getpid());
            foo();
        } else {
            printf("child PID is %d\n", getpid());
            foo();
        }
    } else {
        if (fork() == 0) {
            printf("child PID is %d\n", getpid());
            foo();
        } else {
            printf("parent PID is %d\n", getpid());
            foo();
        }
    }
    return 0;
}

// fork가 된 순간 동일한 코드를 실행하는 자식 프로세스가 생성되었다