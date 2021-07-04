//숫자의 합
#include <iostream> 
using namespace std;
int main()
{
	int num;
	char input;
	int sum = 0;

	cin >> num;

	for (int i = 0; i < num; i++)
	{
		cin >> input;
		sum += (input - 48);
	}
	cout << sum;
}





