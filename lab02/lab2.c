#include <stdio.h>
#include <math.h>

int main()
{
    double x, y, h;
    x = 0.0;
    scanf("%lf", &h);
    int n, k = 0;
    n = 2 / h;
    while (k <= n)
    {
        if (x >= 0 && x <= 1)
          y = cos(x + x * x * x);  
        if (x > 1 && x <= 2)
          y = exp(-x * x) - x * x + 2 * x;  
        printf("%lf %lf\n", x, y);
        x += h;
        k += 1;
    }
}
