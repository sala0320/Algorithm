#N : 0, S : 1, K : 회전 횟수 (회전 시킨 톱니바퀴의 번호, 방향)
#최종 톱니바퀴의 상태 점수 출력
from collections import deque
topni = [deque(map(int, input())) for _ in range(4)]
K = int(input())
cmd = [(map(int, input().split())) for _ in range(K)]

for who, how in cmd:
    w = who - 1
    turn = [0,0,0,0]
    turn[w] = how
    
    #왼쪽
    for i in range(w, 3):
        if turn[i] != 0:
            if topni[i][2] != topni[i+1][6]:
                turn[i+1] = (turn[i] * -1)

    #오른쪽
    for i in range(w, 0, -1):
        if turn[i] != 0:
            if topni[i][6] != topni[i-1][2]:
                turn[i-1] = (turn[i] * -1)
    
    #회전
    for i, t in enumerate(turn):
        if t == 1:
            topni[i].rotate(1)
        elif t == -1:
            topni[i].rotate(-1)


result = 0
for i, top in enumerate(topni):
    if top[0] == 1:
        result += (2 ** i)
print(result)
 

