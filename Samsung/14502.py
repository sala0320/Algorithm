#0 빈칸 1 벽 2 바이러스
#바이러스 상하좌우로 인접한 빈칸으로 퍼져나갈수 있음
#벽 3개 새로 세워야 함
#0칸 개수의 최댓값
import copy
from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direct = [[1,0], [-1,0], [0,1], [0,-1]]

result = []
start = []
empty = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            start.append((i, j))
        if board[i][j] == 0:
            empty.append((i, j))
def check(vb):
    queue = deque(start)

    while(queue):
        x, y = queue.popleft()
        for d in direct:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if vb[nx][ny] == 0:
                vb[nx][ny] = 2
                queue.append((nx, ny))

    result = sum([b.count(0) for b in vb])
    return result

def combi(arr, n):
    result = []
    if len(arr) < n:
        return result

    if n == 1:
        for a in arr:
            result.append([a])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for temp in combi(arr[i+1:], n-1):
                result.append([arr[i]] + temp)

    return result

def virus():
    comb_list = combi(empty, 3)
    max_result = 0

    for comb in comb_list:
        virus_board = copy.deepcopy(board)
        # print(comb)
        for c in comb:
            virus_board[c[0]][c[1]] = 1

        result = check(virus_board)
        # print(result)
        if result > max_result:
            max_result = result

    return max_result

print(virus())