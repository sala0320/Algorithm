# NxN:(2<=100) 정사각 보드 K: 사과 개수
# L(1<=100): 뱀의 방향 변환 횟수
# X(<=10000): 게임시작 시간으로부터 X초가 지난 뒤
# C: 'L'좌 'D'우로 90도 방향 회전
# 초기설정 : 뱀길이 1, 뱀위치 (0,0), 오른쪽으로 향해있음
# 조건 : 이동한 칸에 사과 O -> 사과 X + 꼬리 늘어남 / 이동한 칸에 사과 X -> 꼬리 줄이기
#        뱀 매초마다 이동 / 뱀이 벽또는 자기자신의 몸과 부딪히면 종료
# 출력 : 게임이 끝나는 시간

#주의할 점 1. 시간 더하기 마지막에!

#보드 [사과 유무, 뱀 유무]
from collections import deque
N = int(input())
board = [[[0,0] for i in range(N)] for j in range(N)]
#사과
K = int(input())
for k in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1][0] = 1

#방향전환
C = int(input())
turn = [list(input().split()) for _ in range(C)]

#뱀이 움직이는 방향 (우, 상, 좌, 하)
move = [[0,1], [-1,0], [0,-1], [1,0]]
#뱀이 현재 이동하는 방향
direction = 0
#뱀의 현재 위치
now = deque([[0,0]])
#움직인 시간
time = 1 

while(1):
    
    nx = now[-1][0] + move[direction][0]
    ny = now[-1][1] + move[direction][1]

    print("[ " + str(nx) + ", " + str(ny) + " ]")
    if (nx >= N) or (ny >= N) or (nx < 0) or (ny < 0) or (board[nx][ny][1] == 1):
        print(time)
        break

    else:
        #뱀 위치에 추가 및 보드에 뱀 위치 추가
        now.append([nx, ny])
        board[nx][ny][1] = 1
        #보드에 사과 없으면
        if board[nx][ny][0] == 0:
            #뱀 꼬리 축소 및 보드에서 뱀 위치 삭제
            back = now.popleft()
            board[back[0]][back[1]][1] = 0
        else:
            #보드에서 사과 삭제
            board[nx][ny][0] = 0

    #방향 전환
    if (len(turn) > 0) and (int(turn[0][0]) == time):
        d = turn[0][1]
        turn.pop(0)
        if d == 'D':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        # if (direction == 0 and d == 'D') or (direction == 2 and d == 'L'):
        #     direction = 3
        # elif (direction == 0 and d == 'L') or (direction == 2 and d == 'D'):
        #     direction = 1
        # elif (direction == 1 and d == 'D') or (direction == 3 and d == 'L'):
        #     direction = 0
        # elif (direction == 1 and d == 'L') or (direction == 3 and d == 'D'):
        #     direction = 2

    time += 1

        