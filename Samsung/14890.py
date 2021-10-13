#길에 속한 모든 칸의 높이가 모두 같아야 지나갈 수 있음
#경사로를 놓아서 지나갈 수 있는 길 만들디
#경사로 놓을 수 있는 조건
#1. 낮은칸과 높은 칸의 차이 1
#2. 경사로를 놓은 낮은 칸의 높이는 모두 같음
#3. 경사로를 놓은 L개의 칸이 연속되어있어야 함
#경사로를 놓을 수 없는 조건
#1. 경사로 놓은 곳에 또 경사로 놓기
#2. 낮은칸과 높은칸의 차이가 1이 아닌 경우
#3. 낮은 지점의 칸의 높이가 모두 같지 않고, L 개가 연속되지 않은 경우
N, L = map(int, input().split())
board_x = [list(map(int, input().split())) for _ in range(N)]
board_y = list(map(list, zip(*board_x)))
result = 0


def check(board):
    visited = [False] * N
    connected = [0] * N

    if len(set(board)) == 1:
        return 1

    for i in range(N):
        #내리막길
        if i - 1 >= 0:
            if board[i-1] - board[i] > 1:
                return 0
            if board[i-1] - board[i] == 1:
                for idx in range(L):
                    # 경사로 범위 벗어나면 0반환
                    if (i + idx) >= N:
                        return 0
                    #경사로 이미 설치된 곳이면 0 반환
                    if visited[i+idx] == True:
                        return 0
                    #연속적이지 않으면 0 반환
                    if board[i + idx] != board[i]:
                        return 0
                    visited[i+idx] = True

                    #경사로 설치 시 연결된 경우
                    idx = i-1
                    while (idx >= 0) and (board[idx] == board[i-1]):
                        connected[idx] = 1
                        idx -= 1
                    idx = i
                    while(idx < N) and (board[idx] == board[i]):
                        connected[idx] = 1
                        idx += 1

        if i + 1 < N:
            #오르막길
            if board[i] - board[i + 1] < -1:
                return 0
            if board[i] - board[i+1] == -1:

                for idx in range(L):
                    if (i - idx) < 0:
                        return 0
                    if visited[i-idx] == True:
                        return 0
                    if board[i - idx] != board[i]:
                        return 0
                    visited[i - idx] = True

                idx = i
                while (idx >= 0) and (board[idx] == board[i]):
                    connected[idx] = 1
                    idx -= 1
                idx = i + 1
                while (idx < N) and (board[idx] == board[i+1]):
                    connected[idx] = 1
                    idx += 1

    if sum(connected) == N:
        # print(board)
        return 1
    else:
        return 0

for i in range(N):
    result += check(board_x[i])
    result += check(board_y[i])

print(result)

