#include <iostream>
#include <algorithm>
#include<string>
using namespace std;
int main()
{
	string num1, num2;
	cin >> num1 >> num2;

	reverse(num1.begin(), num1.end());
	reverse(num2.begin(), num2.end());

	cout << max(stoi(num1), stoi(num2));
}