from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

finish = (N - 1, M - 1)
start = (0, 0, 1, 0)
result = -1


def bfs(start):
    global result, visited
    queue = deque([start])
    visited[start[0]][start[1]][0] = 1

    while (queue):
        # print(queue)
        x, y, distance, door = queue.popleft()
        if (x, y) == finish:
            visited = [[0 for _ in range(M)] for _ in range(N)]
            result = max(result, distance)
            return result

        for d in dir:
            nx, ny = x + d[0], y + d[1]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if visited[nx][ny][door] == 0:
                    if board[nx][ny] == 1:
                        if door == 0:
                            visited[nx][ny][door] = 1
                            queue.append((nx, ny, distance + 1, door + 1))
                    else:
                        visited[nx][ny][door] = 1
                        queue.append((nx, ny, distance + 1, door))
    return result


print(bfs(start))