#include <stdio.h>
#include <unistd.h>

// 동일한 작업(foo 함수 실행)을 수행토록 자식 프로세스를 생성할 수도 있다.

void foo() {
    printf("executed foo()!!!\n");
}

int main()
{
    if (fork() == 0) {
        printf("child PID is %d\n", getpid());
        foo();
    } else {
        printf("parent PID is %d\n", getpid());
        foo();
    }
    return 0;
}

// fork가 된 순간 동일한 코드를 실행하는 자식 프로세스가 생성되었다