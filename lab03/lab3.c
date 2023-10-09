#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void fill(int n, int a[])
{
    int i;
    for (i = 0; i < n; i++)
        a[i] = rand () % 101 - 50;
}

int main()
{
    srand(time(NULL));
    int n, imin, imax, min, max;
    min = 52;
    max = 0;
    printf("n -> ");
    scanf("%d", &n);
    int A[n];
    fill(n, A);
    int i;
    for (i = 0; i < n; i++)
        {   
            if (A[i] > max)
                {
                    max = A[i];
                    imax = i;
                }
            if (A[i] < min)
                {
                    min = A[i];
                    imin = i;
                }
            printf("%4d", A[i]);
        }
    printf("\n");
    printf("Индекс минимального элемента -> %d\n", imin);
    printf("Минимальный элемент -> %d\n", min);
    printf("Индекс максимального элемента -> %d\n", imax);
    printf("Максимальный элемент -> %d\n", max);
    printf("Сумма индексов -> %d\n", imin + imax);
    if ((imin + imax) < fabs(min))
        A[imin] = imin + imax;
    else if ((imin + imax) > fabs(max))
        A[imax] = imin + imax;
    else
        {
            if (imin < imax)
                for (i = imin + 1; i < imax && i > imin; i++)
                    A[i] = 0;
            if (imin > imax)
                for (i = imax + 1; i < imin && i > imax; i++)
                    A[i] = 0;         
        }
    printf("Результат: \n");
    for (i = 0; i < n; i++)
        printf("%4d", A[i]);
    printf("\n");
}

