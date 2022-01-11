import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
#정점, 간선
V, E = map(int, input().split())
K = int(input())
graph_input = [list(map(int, input().split())) for _ in range(E)]
#(u, v, w) : u->v : w
graph = [[] for _ in range(V+1)]
for gi in graph_input:
    graph[gi[0]].append((gi[1], gi[2]))
distance = [INF] * (V+1)
def dijkstra(k):
    queue = []
    heapq.heappush(queue, (0, k))
    distance[k] = 0
    while(queue):
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for g in graph[now]:
            new_cost = cost + g[1]
            if new_cost < distance[g[0]]:
                distance[g[0]] = new_cost
                heapq.heappush(queue, (new_cost, g[0]))

dijkstra(K)
for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)