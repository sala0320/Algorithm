#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int N, M;
    int N_num[100000], M_num[100000];
    int result[100000];

    scanf("%d", &N);
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &N_num[i]);
    }
    scanf("%d", &M);
    for(int i = 0; i < M; i++)
    {
        scanf("%d", &M_num[i]);
    }
    sort(N_num, N_num+N);
    for(int i = 0; i < M; i++)
    {   
        if(binary_search(N_num, N_num + N, M_num[i]))
            printf("1\n");
        else
            printf("0\n");
    }
}