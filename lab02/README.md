int main()
{
    double x, y, h;
    x = 0.0;
    scanf("%lf", &h);
    do
    {
        if (x >= 0 & x <= 1)
        {
            y = cos(x + pow(x, 3));
            printf("%f %f\n",x,y);
        }
        x = x + h;
    }while (x <= 1);
    do
    {
        if (x > 1 & x <= 2)
        {
            y = exp(-1 * pow(x, 2)) - pow(x, 2) + 2 * x;
            printf("%f %f\n",x,y);
        }
        x = x + h;
    }while (x <= 2);
}
