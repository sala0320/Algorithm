from collections import deque
import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
result = 0
#Grouping
def dfs(x, y, visited):
    idx = [x, y]
    now = board[x][y]
    queue = deque([[x, y]])
    visited[x][y] = True
    zero_visited = [list(False for _ in range(N)) for _ in range(N)]
    num = 1
    zero_num = 0
    while(queue):
        x, y = queue.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == False and zero_visited[nx][ny] == False:
                #board[x][y]가 0일때도 처리해야할까?
                if board[nx][ny] == 0 or board[nx][ny] == now:
                    num += 1

                    queue.append([nx, ny])
                    if board[nx][ny] == now:
                        idx = [nx, ny]
                        visited[nx][ny] = True
                    if board[nx][ny] == 0:
                        zero_num += 1
                        zero_visited[nx][ny] = True
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
            if visited[i][j] == True or board[i][j] <= 0:
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


    return max_num, max_idx

def gravity(board):
    for j in range(N):
        zero_count = 0
        for i in range(N-1, 0, -1):
            if board[i][j] == -2:
                # if board[i-1][j] == '-1':
                #     continue
                if board[i-1][j] == -2:
                    zero_count += 1
                elif board[i-1][j] >= 0:
                    board[i+zero_count][j] = board[i-1][j]
                    board[i-1][j] = -2
    return


while(True):
    num, idx = find_block(board)
    if num < 2:
        print(result)
        break
    result += num ** 2
    remove(idx[0], idx[1])


    gravity(board)

    temp = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            board[N - 1 - j][i] = temp[i][j]


    gravity(board)
