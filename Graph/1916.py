#다익스트라
import heapq
INF = 1e9
N = int(input())
M = int(input())

graph = [[] for _ in range(N)]
distance = [INF] * (N)
for _ in range(M):
    s, d, c = map(int, input().split())
    graph[s-1].append((d-1, c))

start, dist = map(int, input().split())

def dijkstra(s_node):
    q = []
    #heapq <- (cost, node)
    heapq.heappush(q, (0, s_node))
    distance[s_node] = 0
    while(q):
        cost, n_node = heapq.heappop(q)
        if distance[n_node] < cost:
            continue
        #graph[n_node] = n_node에 연결된 노드들 ([cost, node],[],,)
        for n in graph[n_node]:
            new_cost = cost + n[1]
            if new_cost < distance[n[0]]:
                distance[n[0]] = new_cost
                heapq.heappush(q, (new_cost, n[0]))
    
                      
dijkstra(start-1)
print(distance[dist-1])