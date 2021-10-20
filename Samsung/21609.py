from collections import deque
import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
print(board)
result = 0
#Grouping
def dfs(x, y, visited):
    idx = [x, y]
    now = board[x][y]
    queue = deque([[x, y]])
    visited[x][y] = True
    num = 1
    zero_num = 0
    while(queue):
        x, y = queue.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == False:
                #board[x][y]가 0일때도 처리해야할까?
                if board[nx][ny] == 0 or board[nx][ny] == now:
                    num += 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    if board[nx][ny] == now:
                        idx = [nx, ny]
                    if board[nx][ny] == 0:
                        zero_num += 1
    return num, idx, zero_num

#Removing
def remove(x,y):
    rm_visited = [list(False for _ in range(N)) for _ in range(N)]
    now = board[x][y]
    board[x][y] = -2
    queue = deque([[x, y]])
    rm_visited[x][y] = True
    while (queue):
        x, y = queue.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if rm_visited[nx][ny] == False:
                # board[x][y]가 0일때도 처리해야할까?
                if board[nx][ny] == 0 or board[nx][ny] == now:
                    board[nx][ny] = -2
                    rm_visited[nx][ny] = True
                    queue.append([nx, ny])
    return

def find_block(board):
    global result
    visited = [list(False for _ in range(N)) for _ in range(N)]
    max_num = 0
    max_idx = [0, 0]
    max_zero = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == True or board[i][j] == -1:
                continue
            ret_num, ret_idx, ret_zero = dfs(i, j, visited)
            if ret_num > max_num:
                max_num = ret_num
                max_idx = ret_idx
                max_zero = ret_zero
            elif ret_num == max_num:
                if ret_zero > max_zero:
                    max_num = ret_num
                    max_idx = ret_idx
                    max_zero = ret_zero
                if ret_zero == max_zero:
                    if ret_idx[0] > max_idx[0]:
                        max_num = ret_num
                        max_idx = ret_idx
                        max_zero = ret_zero
                    elif ret_idx[0] == max_idx[0]:
                        if ret_idx[1] > max_idx[1]:
                            max_num = ret_num
                            max_idx = ret_idx
                            max_zero = ret_zero
    print(max_num)
    print(max_idx)
    result += max_num ** 2
    remove(max_idx[0], max_idx[1])
    return

def gravity(board):



find_block(board)
print(board)

gravity(board)
print(board)

new_board = [list(0 for _ in range(N)) for _ in range(N)]
for i in range(N):
    for j in range(N):
        new_board[N - 1 - j][i] = board[i][j]
print(new_board)

#gravity생각해보기!!!!
gravity(new_board)
print(new_board)

print(result)