V, E = int(input()), int(input())
cost = [list(map(int, input().split())) for i in range(E)]
cost.sort(key=lambda x : x[2])
parent = [i for i in range(V+1)]
result = 0
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        parent[p_b] = p_a

for c in cost:
    if find(c[0]) != find(c[1]):
        union(c[0], c[1])
        result += c[2]

print(result)