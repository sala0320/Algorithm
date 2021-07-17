#include <cstdio>
#include <vector>
#define INF 99999999
using namespace std;
int N, M;
vector<pair<int,int>>v[502];
long long dist[501] = {INF,};
int main()
{
    int a,b,c;
    scanf("%d %d", &N,&M);
    while(M--)
    {
        scanf("%d %d %d", &a, &b, &c);
        v[a].push_back(make_pair(b,c));    
    }
    for(int i = 0; i <= N; i++)
    {
        dist[i] = INF;
    }

    bool cycle = false;
    dist[1] = 0;
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            for(int k = 0; k < v[j].size(); k++)
            {
                int cur = v[j][k].first;
                int cost = v[j][k].second;
                if(dist[j] != INF && j != cur && dist[cur] > cost + dist[j])
                {
                    dist[cur] = cost + dist[j];
                    if(i == N)
                        cycle = true;
                }
            }
        }
    }
    if(cycle)
        printf("%d\n", -1);
    else
    {
        for(int i=2; i<= N; i++)
        {
            if(dist[i] == INF)
                printf("%d\n", -1);
            else
                printf("%d\n", dist[i]);
        }
    }
    return 0;
}