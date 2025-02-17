# include <stdio.h>

int plus(int a, int b) {
    return a + b;
}

int minus(int a, int b) {
    return a - b;
}

int call(int (*p)(int, int), int a, int b) {
    return p(a, b);
}

int main()
{
    int a = 100;
    int b = 200;

    int result = call(plus, a, b);
    printf("=> %d\n", result);

    return 0;
}