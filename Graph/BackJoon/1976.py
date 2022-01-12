N = int(input())
M = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
parent = [0] * N
for i in range(N):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = find(a)
    else:
        parent[a] = find(b)

def solve(trip):
    for k in range(M-1):
        if find(trip[k]-1) != find(trip[k+1]-1):
            return 1
    return 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            union(i, j)
# print(parent)
trip = list(map(int, input().split()))
if solve(trip) == 0:
    print("YES")
else:
    print("NO")


    

