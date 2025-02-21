#include <stdio.h>
#include <unistd.h>

// 각기 다른 작업을 하는 프로세스 생성하기
void foo() {
    printf("execute foo()!!!\n");
}

void bar() {
    printf("execute bar()!!!\n");
}

void baz() {
    printf("execute baz()!!!\n");
}

int main()
{
    if (fork() == 0) {
        if (fork() == 0) {
            foo();
        } else {
            bar();
        }
    } else {
        baz();
    }
    return 0;
}

// fork가 된 순간 동일한 코드를 실행하는 자식 프로세스가 생성되었다