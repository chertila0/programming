#include <stdio.h>

int main()
{
    int a, b, s;
    printf("Введите a -> ");
    scanf("%d", &a);
    printf("Введите b -> ");
    scanf("%d", &b);
    s = a / 10.0 + a % 10;
    if (s > b)
        printf("%d\n", s);
    if (s < b)
        printf("%d\n", s + b);
    if (s == b)
        printf("Сумма цифр = %d\n", b);
}