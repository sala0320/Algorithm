from collections import deque
N, M, V = list(map(int, input().split()))
board = [[0] * (N) for _ in range(N)]
for _ in range(M):
    ip = list(map(int, input().split()))
    board[ip[0]-1][ip[1]-1] = 1
    board[ip[1]-1][ip[0]-1] = 1

def dfs(start):
    visited[start] = 1
    print(start+1, end=" ")
    for i in range(N):
        if board[start][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while(queue):
        now = queue.popleft()
        print(now + 1, end=" ")
        for i in range(N):
            if board[now][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1


visited = [0 for _ in range(N)]
dfs(V-1)
visited = [0 for _ in range(N)]
print()
bfs(V-1)