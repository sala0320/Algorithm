//5로 나누어질때 까지 3 빼기
#include <iostream>
using namespace std;
int main()
{
	int N, count = 0;
	cin >> N;

	while (N > 0)
	{
		if (N % 5 == 0)
		{
			count += N / 5;
			break;
		}
		N -= 3;
		count++;
	}
	if (N < 0)
		cout << -1;
	else
		cout << count;


}



