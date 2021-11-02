from collections import deque
import sys
T = int(input())
dir = [[-1,-2], [-2,-1], [-2,1], [-1,2], [1,-2], [2,-1], [2,1], [1,2]]

def bfs(start, finish):
    queue = deque([start + [0]])
    while(queue):
        # print(queue)
        x, y, c = queue.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if nx == finish[0] and ny == finish[1]:
                print(c+1)
                return
            if visited[nx][ny] == 0:
                queue.append([nx, ny, c+1])
                visited[nx][ny] = 1
for _ in range(T):
    l = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    finish = list(map(int, sys.stdin.readline().split()))
    visited = [[0 for _ in range(l)] for _ in range(l)]
    visited[start[0]][start[1]] = 1
    if start != finish:
        bfs(start, finish)
    else:
        print(0)