#include <iostream>
#include <vector>
using namespace std;
int isPrime(int num)
{
	if (num == 1)
		return 0;
	else
	{
		for (int i = 2; i < num; i++)
		{
			if (num % i == 0)
				return 0;
		}
		return 1;
	}
}
int main()
{
	int M, N;
	int sum = 0, min = 10000;
	cin >> M >> N;
	for (int i = M; i <= N; i++)
	{
		if (isPrime(i) == 1)
		{
			sum += i;
			if (min > i)
				min = i;
		}
	}
	if (sum == 0)
		cout << -1;
	else
	{
		cout << sum << "\n";
		cout << min << "\n";
	}

}