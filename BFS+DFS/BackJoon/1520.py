#DFS + DP
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1 for _ in range(N)] for _ in range(M)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]

def dfs(x,y,w):
    if x == M-1 and y == N-1:
        return 1
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        nw = board[nx][ny]


        if nw < w and visited[nx][ny] == -1:
            (nx,ny,nw)

dfs(0,0,board[0][0])
print(count)

