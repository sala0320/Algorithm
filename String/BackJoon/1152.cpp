//isspace: 공백유무함수이용하기

#include <iostream> 
#include <string>
#define MAX 1000000
using namespace std;
int main()
{
	string str;
	int len, count = 0;

	getline(cin, str);
	len = str.length();

	for (int i = 0; i < len; i++)
	{
		if (str[i] == ' ')
			count++;
	}
	if (isspace(str[0]))
		count--;
	if (isspace(str[len - 1]))
		count--;

	cout << count + 1;
}





