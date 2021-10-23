from collections import deque
import math
N, M, K = map(int, input().split())
fireball = deque([list(map(int, input().split())) for _ in range(M)])
dir = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
board = [[[] for _ in range(N)] for _ in range(N)]
#setting
for f in fireball:
    f[0] -= 1
    f[1] -= 1
    board[f[0]][f[1]] = f

for i in range(K):
    #fireball move
    board = [[[] for _ in range(N)] for _ in range(N)]
    while(fireball):
        r,c,m,s,d = fireball.popleft()

        nr = (r + (dir[d][0] * s) + N ) % N
        nc = (c + (dir[d][1] * s) + N ) % N

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        board[nr][nc].append([nr, nc, m, s, d])

    two = deque([])
    for i in range(N):
        for j in range(N):
            #2개 이상일때
            if len(board[i][j]) > 1:
                ball = board[i][j]
                num_ball = len(ball)
                total_m = 0
                total_s = 0
                count_d = 0
                for b in ball:
                    total_m += b[2]
                    total_s += b[3]
                    if b[4] % 2 == 0:
                        count_d += 1
                for idx in range(4):
                    if count_d == 0 or count_d == num_ball:
                        idx = idx * 2
                    else:
                        idx = (idx * 2) + 1
                    m = int(total_m / 5)
                    s = int(total_s / num_ball)
                    if m != 0:
                        fireball.append([i, j, m, s, idx])
            #1개일때
            elif len(board[i][j]) == 1:
                if board[i][j][0][2] != 0:
                    fireball.append(board[i][j][0])

print(sum(fb[2] for fb in fireball))
