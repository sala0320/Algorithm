import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + board[i][j] - dp[i][j]
print(dp)
question = []
for _ in range(M):
    question.append(list(map(int, input().split())))

for q in question:
    result = dp[q[2]][q[3]] - dp[q[0]][q[1]] + board[q[0]-1][q[1]-1]
    print(dp[q[2]][q[3]],dp[q[0]][q[1]],board[q[0]-1][q[1]-1])
    print(result)
