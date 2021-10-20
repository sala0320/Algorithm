import copy
N = int(input())
student = [list(map(int, input().split())) for _ in range(N**2)]
board = [[0 for _ in range(N)] for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
for s in range(len(student)):
    max_like = 0
    max_empty = 0
    best_seat = [0, 0]
    init = 0
    for i in range(N):
        for j in range(N):
            near = []
            like = 0
            empty = 0
            if board[i][j] == 0:
                if init == 0:
                    best_seat = [i, j]
                    init += 1
                for d in dir:
                    nx = i + d[0]
                    ny = j + d[1]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue

                    if board[nx][ny] == 0:
                        empty += 1

                    if board[nx][ny] in student[s][1:]:
                        like += 1

                if like > max_like:
                    max_like = like
                    max_empty = empty
                    best_seat = [i, j]
                elif like == max_like:
                    if empty > max_empty:
                        max_empty = empty
                        best_seat = [i, j]

    board[best_seat[0]][best_seat[1]] = student[s][0]
student.sort()
result = 0
for i in range(N):
    for j in range(N):
        likes = 0
        for d in dir:
            nx = i + d[0]
            ny = j + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] in student[board[i][j]-1][1:]:
                likes += 1
        if likes == 1:
            result += 1
        elif likes == 2:
            result += 10
        elif likes == 3:
            result += 100
        elif likes == 4:
            result += 1000
print(result)
