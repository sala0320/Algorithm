from collections import deque
N = int(input())
#0 빈칸, 1~6 물고기의 크기, 9 아기상어의 위치
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
#아기상어 위치 및 크기
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            fish = (i, j, 0)
            board[i][j] = 0
eat = 0
size = 2
time = 0
def bfs(fish):
    global eat, size, time
    queue = deque([fish])
    # print(queue)
    eat_list = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    while(queue):
        x, y, t = queue.popleft()

        visited[x][y] == True
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == False:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny, t+1])
                elif board[nx][ny] == size:
                    queue.append([nx, ny, t+1])
                    visited[nx][ny] = True
                elif board[nx][ny] < size:
                    eat_list.append([nx, ny, t+1])
                    visited[nx][ny] = True

    eat_list.sort(key = lambda x:(x[2], x[0], x[1]))
    if len(eat_list) == 0 or sum(sum(b) for b in board) == 0:
        return [-1, time]
    else:
        time += eat_list[0][2]
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        board[eat_list[0][0]][eat_list[0][1]] = 0
        eat_list[0][2] = 0
        return eat_list[0]

while(True):

    if fish[0] == -1:
        print(fish[1])
        break
    fish = bfs(fish)

