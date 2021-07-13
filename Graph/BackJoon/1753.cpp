#include<cstdio>
#include<queue>
#include<vector>
#define MAX 20010
#define INF 987654321
using namespace std;
vector<pair<int, int>> graph[MAX];
int main()
{
    int V, E, S;
    scanf("%d %d", &V, &E);
    scanf("%d",&S);

    //모든 간선 정보 받기
    for(int i = 0; i < E; i++)
    {
        int u,v,w;
        scanf("%d %d %d", &u, &v, &w);
        //u에서 v로 가는 비용이 w
        graph[u].push_back(make_pair(v,w));
    }   
    //최단거리테이블을 모두 무한으로 초기화 
    int distance[V+1];
    for(int i = 1; i <= V; i++)
        distance[i] = INF;
    
    //다익스트라
    priority_queue<pair<int, int>> pq;
    pq.push(make_pair(0,S));
    distance[S] = 0;

    //큐가 비어있지 않을 동안
    while(!pq.empty())
    {
        //가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        for(int i = 0; i < graph[now].size(); i++)
        {
            int next = graph[now][i].first;
            int ndist = graph[now][i].second;

            if(distance[next] > dist + ndist)
            {
                distance[next] = dist + ndist;
                pq.push(make_pair(-distance[next], next));
            }
        }
    }
    //출력
    for(int i = 1; i <= V; i++)
    {
        if(distance[i] == INF)
            printf("INF\n");
        else    
            printf("%d\n", distance[i]);
    }
}

