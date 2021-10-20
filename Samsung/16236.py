#NxN공간, 물고기M, 아기상어 1
#가장 처음 아기 상어의 크기는 2 -> 1초에 상하좌우로 이동
#단 거리가 가까운 물고기를 먹으러 가는 방향으로 움직임
#거리 동일 -> 가장 위에 있는 물고기 -> 가장 왼쪽에 있는 물고기

#자신보다 큰 물고기가 있는 칸을 지나갈 수 없음
#자신보다 작은 물고기는 먹을 수 있음
#자신과 크기가 같은 물고기는 먹을 수 없지만 지나갈 수 있음
#자신의 크기와 같은 수의 물고기를 먹으면 아기 상어의 크기가 1 증가

#몇초동안 물고기를 먹을 수 있는지 -> 물고기가 없거나, 도달할 수 없거나, 상어보다 작은게 없거나

#입력
#2<= N <= 20
from collections import deque
N = int(input())
#0 빈칸, 1~6 물고기의 크기, 9 아기상어의 위치
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
#아기상어 위치 및 크기
fish = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = [i, j, 2, 0, 0]
            board[i][j] = 0
        if board[i][j] > 0 and board[i][j] < 7:
            fish.append([i, j, board[i][j]])
if fish == 0:
    print(0)
else:









