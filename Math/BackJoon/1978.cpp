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
	int N;
	int num, count = 0;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> num;
		if (isPrime(num) == 1)
			count++;
	}
	cout << count;

}