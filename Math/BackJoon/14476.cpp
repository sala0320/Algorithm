//왼쪽에서 오른쪽으로 진행하면서 gcd
//오른쪽에서 왼쪽으로 진행하면서 gcd
#include <cstdio>
int n, arr[1000001],ltor[1000001],rtol[1000001];
using namespace std;

int gcd(int a, int b) {
	while (b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}
int main()
{
    scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	ltor[0] = arr[0];
	for (int i = 1; i < n; i++) {
		ltor[i] = gcd(ltor[i - 1], arr[i]);
	}
	rtol[n - 1] = arr[n - 1];
	for (int i = n-2; i >=0; i--) {
		rtol[i] = gcd(rtol[i+1], arr[i]);
	}
    int ans = 0;
    int temp_gcd = 0;
    int gcd_ans = 0;
    for(int i = 0; i < n; i++)
    {
        temp_gcd = gcd(ltor[i-1], rtol[i+1]);
        if(arr[i] % temp_gcd !=0 && temp_gcd > ans)
        {
            ans = arr[i];
            gcd_ans = temp_gcd;
        }
    }
    if(ans == 0 && gcd_ans == 0)
        printf("-1\n");
    else    
        printf("%d %d\n", gcd_ans, ans);

    return 0;
}