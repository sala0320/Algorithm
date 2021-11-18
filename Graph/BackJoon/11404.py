#플루이드 와샬
INF = 1e9
N = int(input())
M = int(input())
bus = [[INF]*(N) for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    bus[a-1][b-1] = min(bus[a-1][b-1], c)
for n in range(N):
    bus[n][n] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

for a in range(N):
    for b in range(N):
        if bus[a][b] == INF:
            print(0, end=" ")
        else:
            print(bus[a][b], end=" ")
    print()
            


