//알파벳 찾기
//같은 문자일떄는 처음 문자로
#include <iostream> 
#include <cstring>
using namespace std;
int main()
{
	char str[100];
	int alp[26];
	cin >> str;

	for (int i = 0; i < 26; i++)
	{
		alp[i] = -1;
	}
	for (int i = 0; i < strlen(str); i++)
	{
		if (alp[str[i] - 'a'] == -1)
		{
			alp[str[i] - 'a'] = i;
		}
	}
	for (int i = 0; i < 26; i++)
	{
		cout << alp[i] << " ";
	}
}





