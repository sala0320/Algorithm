#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
vector<int> graph[32001]; //노드에서 나가는 간선 나타낸 벡터
int indegree[32001]; //노드에 들어오는 간선의 수 나타낸 배열
queue<int> q; //indegree담을 큐
int main()
{
    int N, M; //N:노드 수, M:간선 수
    scanf("%d %d", &N, &M);
    for(int i=0; i < M; i++)
    {
        int a,b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
    }

    for(int i = 1; i <= N; i++)
    {
        if(indegree[i] == 0)
            q.push(i);
    }
    while(!q.empty())
    {
        int cur = q.front();
        q.pop();
        printf("%d ", cur);

        for(int i=0; i < graph[cur].size(); i++)
        {
            int next = graph[cur][i];
            indegree[next]--;
            if(indegree[next] == 0)
                q.push(next);
        }           
    }
    return 0;
}