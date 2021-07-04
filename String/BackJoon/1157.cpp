//strlen for문에 넣으면 시간초과 나오므로 int len으로 선언해두기

#include <iostream> 
#include <cstring>
#define MAX 1000000
using namespace std;
int main()
{
	char str[MAX];
	int alph[26] = { 0 };
	int max = 0, same = 0, maxNum;

	cin >> str;
	int len = strlen(str);

	for (int i = 0; i < len; i++)
	{
		if (str[i] >= 97 && str[i] <= 122)
		{
			alph[str[i] - 97]++;
		}
		else
		{
			alph[str[i] - 65]++;
		}
	}
	for (int i = 0; i < 26; i++)
	{
		if (max < alph[i])
		{
			max = alph[i];
			maxNum = i;
			same = 0;
		}
		else if (max == alph[i])
		{
			same++;
		}
	}
	if (same > 0)
		printf("?");
	else
		printf("%c", maxNum + 65);
}





