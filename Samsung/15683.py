import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1],[1,0],[0,-1], [-1,0]] #우하좌상
cctv_dir = [4,2,4,4,1]
cctv_ver = [[[0],[1], [2], [3]],
            [[0,2], [1,3]],
            [[0,3], [2,3], [1,2], [0,1]],
            [[0,2,3], [1,2,3], [0,1,2], [0,1,3]],
            [[0,1,2,3]]]
cctv = []
for i in range(N):
    for j in range(M):
        if board[i][j] > 0 and board[i][j] < 6:
            cctv.append((i, j, board[i][j]))

def check(list):
    new_board = copy.deepcopy(board)
    for i, v in enumerate(list):
        new_dir = cctv_ver[cctv[i][2] - 1][v]
        for d in new_dir:
            x, y, c = cctv[i]
            while (True):
                x = x + dir[d][0]
                y = y + dir[d][1]
                if x < 0 or x >= N or y < 0 or y >= M:
                    break
                if board[x][y] == 6:
                    break
                if board[x][y] == 0:
                    new_board[x][y] = c
    sum = 0
    for i in range(N):
        sum += new_board[i].count(0)
    return sum
def dfs(depth, idx, list):
    global Min
    if idx == len(cctv):
        check_num = check(list)
        Min = min(check_num, Min)
        return
    else:
        for i in range(cctv_dir[cctv[idx][2]-1]):
            list.append(i)
            dfs(depth+1, idx+1, list)
            list.pop()
        return
Min = 1e9
dfs(0,0,[])
print(Min)