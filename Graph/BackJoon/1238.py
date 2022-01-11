import heapq
import sys
input = sys.stdin.readline
INF = 1e9
N, M, X = map(int, input().split())
result = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    global distance
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while(queue):
        cost, now = heapq.heappop(queue)
        if cost > distance[now]:
            continue
        for g in graph[now]:
            new_cost = cost + g[1]
            if new_cost < distance[g[0]]:
                distance[g[0]] = new_cost
                heapq.heappush(queue, (new_cost, g[0]))
for i in range(1,N+1):
    distance = [INF] * (N + 1)
    if i == X:
        dijkstra(i)
        for idx, d in enumerate(distance):
            result[idx] += d
    else:
        dijkstra(i)
        result[i] += distance[X]

print(max(result[1:]))

