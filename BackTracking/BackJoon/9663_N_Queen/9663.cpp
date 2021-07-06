#include <iostream>
#define MAX 15
using namespace std;

int col[MAX];
int N, total = 0;

bool check(int level)
{
    /**이전행들에 퀸이 있는 열(col[i])과 지금 퀸을 놓고자 하는 곳의 열(col[level])가 같거나
     * 지금 퀸을 놓고자 하는 위치의 대각선에 퀸이 존재할 때
     * 지금 퀸을 놓고자 하는 곳의 열과 이전 행들에 퀸이 있는 열(col[level]-col[i])의 차이()
     * 지금 퀸을 놓고자 하는 곳의 행과 이전 행들에 퀸이 있는 행(level - i)의 차이가 같을 때**/
    for(int i = 0; i < level; i++)
        if(col[i] == col[level] || abs(col[level] - col[i]) == level - i)
            return false;
       
    return true;
}

void nqueen(int x)
{
    if(x == N)
        total++;
    else
    {
        for(int i = 0; i < N; i++)
        {
            //x 는 x값, col[x]는 y값
            col[x] = i;
            if(check(x))
                nqueen(x+1);
        }
    }
}
int main() {
    cin >> N;
    nqueen(0);
    cout << total;
}