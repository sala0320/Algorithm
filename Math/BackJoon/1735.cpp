//약분되는 경우 고려하기 -> 최대공약수
#include <cstdio>
int gcd(int a, int b)
{
    if(b == 0)
        return a;
    else
        return gcd(b, a % b);
}
int main()
{
    int a,b;
    scanf("%d %d", &a, &b);
    
    int c,d;
    scanf("%d %d", &c, &d);
    
    int p, q, g;
    p = a * d + b * c;
    q = b * d;
    g = gcd(p,q);
    
    printf("%d %d", p/g, q/g);
}