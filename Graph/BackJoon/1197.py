#https://www.acmicpc.net/problem/1197
V, E = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(E)]
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (V+1)
for i in range(V+1):
    parent[i] = i

#세번째 값 기준으로 sort
graph.sort(key=lambda x : x[2])
print(graph)
result = 0
for g in graph:
    a, b, cost = g
    #두 노드 이어져 있지 않으면
    if find(parent, a) != find(parent, b):
        #합치기
        union(parent, a, b)
        result += cost
print(result)
