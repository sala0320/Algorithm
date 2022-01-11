#DFS + DP
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]
visited = [[False for _ in range(N)] for _ in range(M)]
def dfs(x,y,w):
    global count, visited
    print(x, y, w, count, visited)
    if x == M-1 and y == N-1:
        count += 1
        visited = [[False for _ in range(N)] for _ in range(M)]
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        nw = board[nx][ny]
        if nw < w and visited[nx][ny] == False:
            visited[nx][ny] = True
            if board[nx][ny] == -1:
                count += 1
                visited = [[False for _ in range(N)] for _ in range(M)]
            else:
                board[nx][ny] = -1
                dfs(nx,ny,nw)

count = 0
dfs(0,0,board[0][0])
print(board)
print(count)

