
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int N, K;
int alp[26];
int Max;
string word[55];
//N개 문장 돌면서 dfs로 뽑은 문자들이 다 포함되어 있는 문장이 몇개인지 개수 세기
int check()
{
    int sum = 0;
    for(int i = 0; i < N; i++)
    {
        int flag = 1;
        //앞 4개, 뒤 4개는 필수니까 빼고
        for(int j = 4; j < word[i].size()-4; j++)
        {
            if(alp[word[i][j] - 'a'] == 0)
            {
                flag = 0;
                break;
            }
        }
        if(flag == 1)
            sum++;
    }
    return sum;
}
void dfs(int idx, int cnt)
{
    if(cnt == K-5)
    { 
        //dfs로 뽑은 문자들로 만들 수 있는 문장이 최대일때 반환
        Max = max(Max,check());
        return;
    }
    //dfs로 모든 문자 K개씩 묶어서 문장별로 check하기 
    for(int i = idx; i < 26; i++)
    {
        if(alp[i] == 0)
        {
            alp[i] = 1;
            dfs(i, cnt+1);
            alp[i] = 0;
        }
    }
}
int main()
{
    cin >> N >> K;
    
    alp['a' - 'a'] = 1;
    alp['n'- 'a'] = 1;
    alp['t' - 'a'] = 1;
    alp['i'- 'a'] = 1;
    alp['c' - 'a'] = 1;
    
    for(int i = 0; i < N; i++)
        cin >> word[i];

    if(K < 5)
        cout << "0";
    else
    {
        dfs(0,0);
        cout << Max;
    }
}

