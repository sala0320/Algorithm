from collections import deque
N = int(input())
board = [list(map(int, input())) for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
def dfs(x, y):
    global count
    if x >= 0 and x < N and y >= 0 and y < N and board[x][y] == 1:
        board[x][y] = -1
        count += 1
        for d in dir:
            dfs(x+d[0], y+d[1])
    else:
        return

result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)
print(len(result))
result.sort()
for r in result:
    print(r)