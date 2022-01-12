#DFS + DP
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]
dp = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(x, y):
    #끝점에 도달하면 1 반환(끝점에서 끝점까지 갈 수 있는 길은 하나니까)
    if x == M-1 and y == N-1:
        return 1
    #한번도 방문하지 않은 곳이라면
    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= M or ny < 0 or ny >= N: 
                continue
            #다음으로 가는 곳이 지금보다 작으면
            if board[nx][ny] < board[x][y]:
                #dp 현재 위치에서 끝점까지 갈 수 있는 경로의 수 = 다음 위치에서 끝점까지 갈 수 있는 경로의 수들의 합
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0,0))
print(dp)