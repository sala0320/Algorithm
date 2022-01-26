from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
all_dir = [(0, 1), (1, 0)]


def bfs(i, j):

    queue = deque([(i, j)])
    combine = deque([(i, j)])
    combine_sum = board[i][j]
    combine_count = 1
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if L <= abs(board[nx][ny] -
                        board[x][y]) <= R and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

                combine_count += 1
                combine_sum += board[nx][ny]
                combine.append((nx, ny))

    if combine_count > 0:

        for c in combine:
            new_num = combine_sum // combine_count
            board[c[0]][c[1]] = new_num
        return 1
    else:
        return 0


result = 0
while (True):
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for ad in all_dir:
                ni = i + ad[0]
                nj = j + ad[1]
                if ni >= N or nj >= N:
                    continue
                if L <= abs(board[ni][nj] -
                            board[i][j]) <= R and visited[i][j] == 0:
                    count += bfs(i, j)

    if count == 0:
        break
    else:
        result += 1

print(result)
