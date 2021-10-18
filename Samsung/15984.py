N, M, H = map(int, input().split())
board = [[0] * N for _ in range(H)]

for i in range(M):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

def move():
    for n in range(N):
        start = n
        for h in range(H):
            if board[h][start]:
                start += 1
            elif start > 0 and board[h][start - 1]:
                start -= 1
        if start != n:
            return False
    return True

def dfs(count, start, idx):
    global ans
    if idx == count:
        if move():
            ans = count
        return

    for i in range(start, H):
      for j in range(N-1):
        #j=0일때, board[j-1]은 어차피 항상 0 + j = N-1일때,board[j+1]은 항상 0
        if not board[i][j-1] + board[i][j] + board[i][j+1]:
            board[i][j] = 1
            dfs(count + 1, i, idx)
            board[i][j] = 0
ans = 4
for i in range(4):
    dfs(0,0,i)
    if ans < 4:
        break

if ans < 4:
    print(ans)
else:
    print(-1)