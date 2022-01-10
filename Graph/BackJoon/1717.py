#https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(10**5)
#런타임 에러 (RecursionError) 오류 해결
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

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

# for _ in range(m):
#     c, a, b = map(int, input().split())
#     if c == 0:
#         union(parent, a, b)
#     else:
#         if find(parent, a) == find(parent, b):
#             print("YES")
#         else:
#             print("NO")
cmd = [list(map(int, input().split())) for _ in range(m)]
for c in cmd:
    if c[0] == 0:
        union(parent, c[1], c[2])
    else:
        if find(parent, c[1]) == find(parent, c[2]):
            print("YES")
        else:
            print("NO")