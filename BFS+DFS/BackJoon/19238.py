from collections import deque
import sys
input = sys.stdin.readline
N, M, S = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

start = list(map(int, input().split()))
destination = []
for i in range(M):
    customer = list(map(int, input().split()))
    board[customer[0]-1][customer[1]-1] = i+2
    destination.append((customer[2]-1, customer[3]-1))

print(board)
print(start)
print(destination)
dir = [[1,0], [0,1], [-1,0], [0,-1]]
def bfs(sx, sy, sc):
    queue = deque([])
    queue.append((sx, sy, sc))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[start[0]-1][start[1]-1] = 1
    while(queue):
        print(queue)
        x, y, c = queue.popleft()
        if c == 0:
            return -1
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] > 1:
                print(nx, ny, c)
                np = board[nx][ny] - 2
                nc = abs(destination[np][0] - nx) + abs(destination[np][1] - ny)
                board[nx][ny] = 0
                queue.clear()
                queue.append((destination[np][0], destination[np][1], c + nc - 1))
                visited = [[0 for _ in range(N)] for _ in range(N)]
                print(queue)
                print("------------")
            elif board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, c-1))
    return c

print(bfs(start[0]-1, start[1]-1, S))