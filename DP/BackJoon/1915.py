#dp[i][j] = 현재까지 가장 큰 정사각형 한변의 크기
# 1 1 1      1 1 1
# 1 1 1  =>  1 2 2  => 답 : 3
# 1 1 1      1 2 3
# 1 0 1      1 0 1
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(i, j):
    queue = deque([])
    queue.append((i, j))
    dp[i][j] = board[i][j]
    visited[i][j] = 1
    max_num = dp[i][j]

    while (queue):
        x, y = queue.popleft()

        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
                continue

            #배열 가장 왼쪽이나, 상단일 경우
            if nx == 0 or ny == 0 or board[nx][ny] == 0:
                dp[nx][ny] = board[nx][ny]
            #나머지는 왼쪽, 왼쪽 위, 위 세곳 중 가장 작은값에 더하기
            else:
                dp[nx][ny] = min(dp[nx - 1][ny - 1], dp[nx - 1][ny],
                                 dp[nx][ny - 1]) + 1

            max_num = max(max_num, dp[nx][ny])
            queue.append((nx, ny))
            visited[nx][ny] = 1
    print(max_num * max_num)


dfs(0, 0)
