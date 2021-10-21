from collections import deque
import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
result = 0

#해당 x,y에서 시작해서 같은 그룸끼리 묶기
def dfs(x, y, visited):
    idx = [x, y]
    now = board[x][y]
    queue = deque([[x, y]])
    visited[x][y] = True
    #무지개는 초기화해야함!!!!!!
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
                if board[nx][ny] == 0 or board[nx][ny] == now:
                    num += 1
                    queue.append([nx, ny])
                    if board[nx][ny] == now:
                        #행 작을때
                        if idx[0] > nx:
                            idx = [nx, ny]
                        elif idx[0] == nx:
                            #열작을 때
                            if idx[1] > ny:
                                idx = [nx, ny]
                        visited[nx][ny] = True
                    if board[nx][ny] == 0:
                        zero_num += 1
                        zero_visited[nx][ny] = True
    return num, idx, zero_num

#제거하기
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
                if board[nx][ny] == 0 or board[nx][ny] == now:
                    board[nx][ny] = -2
                    rm_visited[nx][ny] = True
                    queue.append([nx, ny])
    return

#모든 행, 열 돌면서 가장 큰 블록찾기
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
            #블록수 가장 큰 것으로
            if ret_num > max_num:
                max_num = ret_num
                max_idx = ret_idx
                max_zero = ret_zero
            elif ret_num == max_num:
                #무지개 많은 것으로
                if ret_zero > max_zero:
                    max_num = ret_num
                    max_idx = ret_idx
                    max_zero = ret_zero
                if ret_zero == max_zero:
                    #행 큰것으로
                    if ret_idx[0] > max_idx[0]:
                        max_num = ret_num
                        max_idx = ret_idx
                        max_zero = ret_zero
                    elif ret_idx[0] == max_idx[0]:
                        #열 큰것으로
                        if ret_idx[1] > max_idx[1]:
                            max_num = ret_num
                            max_idx = ret_idx
                            max_zero = ret_zero
    return max_num, max_idx

#중력
def gravity(board):
    for j in range(N):
        zero_count = 0
        for i in range(N-1, 0, -1):
            if board[i][j] == -2:
                #윗칸도 빈공간이면 빈공간 count 추가
                if board[i-1][j] == -2:
                    zero_count += 1
                #윗값 -1이면 리셋
                elif board[i-1][j] == -1:
                    zero_count = 0
                #윗칸이 빈공간이 아니면 그동안의 빈공간 위에 해당 값 넣기
                elif board[i-1][j] >= 0:
                    board[i+zero_count][j] = board[i-1][j]
                    board[i-1][j] = -2
    return
#돌기
def nturn(board):
    temp = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            board[N - 1 - j][i] = temp[i][j]

while(True):
    num, idx = find_block(board)
    if num < 2:
        break
    result += (num ** 2)
    remove(idx[0], idx[1])
    gravity(board)
    nturn(board)
    gravity(board)

print(result)
