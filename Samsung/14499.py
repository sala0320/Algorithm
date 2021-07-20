# N x M 지도의 좌표 (r, c)
# 주사위가 놓여져 있는 곳의 좌표는 (x, y)
# 1. 주사위를 굴렸을 때 지도위에 쓰여있는 수가 0이면, 주사위 바닥면에 있는 수 복사 
# 2. 0이 아니면 칸에 쓰여있는 수가 주사위 바닥에 복사 + 칸에 쓰인 수는 0
# 주사위를 지도 밖으로 이동시키려 하는 경우 명령 무시 + 출력 없음
# 출력 : 주사위가 이동했을 때 마다 주사위 상단에 쓰여있는 값

#주의 할 점
#1. 동서남북 주사위 이동 잘 체크하기
#2. 예외처리 후 주사위 이동!

#플로우
#1. 예외처리(check) ->주사위 이동(move) -> 보드, 주사위 상태 변경(change) -> 출력

dice_move = [[3,1,0,5,4,2], [2,1,5,0,4,3], [4,0,2,3,5,1], [1,5,2,3,0,4]]
dice = [0,0,0,0,0,0]
X, Y, x, y, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(X)]
cmd = list(map(int, input().split()))

def change(x,y):
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0])

def check(x,y):
    if (x >= X) or (x < 0) or (y >= Y) or (y < 0):
        # print("OUt!!!")
        return False
    return True

def move(c):
    new_dice = [0,0,0,0,0,0]
    for i, d in enumerate(dice_move[c]):  
        new_dice[i] = dice[d]
    return new_dice

for c in cmd:
    if c == 1:
        if check(x,y+1):
            y = y + 1
            dice = move(c-1)
            change(x,y)
        
    elif c == 2:
        if check(x,y-1):
            y = y - 1
            dice = move(c-1)
            change(x,y)
    elif c == 3:
        if check(x-1,y):
            x = x - 1
            dice = move(c-1)
            change(x,y)
    elif c == 4:
        if check(x+1,y):
            x = x + 1
            dice = move(c-1)
            change(x,y)