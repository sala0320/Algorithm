
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int N, K;
int alp[26] = {0,};
int Max;
string word[55];
int count()
{
    int sum = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < word[i+1].size(); j++)
        {
            if(alp[word[i][j] - 'a'] == 0)
            {
                sum += 1;
                return sum;
            }
        }
    }
}
void dfs(int idx, int cnt)
{
    if(cnt == K-5)
    {
        Max = max(Max, count());
    }
    for(int i=idx; i < 26; i++)
    {
        if(alp[i] == 0)
        {
            alp[i] = 1;
            dfs(i+1, cnt+1);
            alp[i] = 0;
        }
    }
}
int main()
{
    cin >> N >> K;
    if(K < 5)
    {
        cout << '0';
    }
    else
    {
        alp['a' - 'a'] = 1;
        alp['n'- 'n'] = 1;
        alp['t' - 't'] = 1;
        alp['i'- 'i'] = 1;
        alp['c' - 'c'] = 1;
        
        for(int i=0; i < N; i++)
        {
            cin >> word[i+1];
        }
        dfs(0,0);
        cout << Max;
    }
}

