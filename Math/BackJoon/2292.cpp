//<2 <8 < 20 ... 6의배수로 더해지는 규칙
#include <iostream>
using namespace std;
int main()
{
	int  N, num = 2, count = 1;
	cin >> N;
	while (1)

	{
		if (N < num)
		{
			cout << count;
			break;
		}
		count++;
		num += (6 * (count - 1));
	}
}
