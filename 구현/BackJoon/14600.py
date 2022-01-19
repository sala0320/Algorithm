K = int(input())
x, y = map(int, input().split())
l = 2**K

board = [[0 for _ in range(l)] for _ in range(l)]
board[l-y][x-1] = -1

#정사각형 내 숫자 있는지 없는지 체크
def check(nx, ny, l):
    global board 
    for i in range(nx, nx + l):
        for j in range(ny, ny + l):
            if board[i][j] != 0:
                return 0
    return 1

#정사각형 나누기
def divide(nx, ny, l, count):
    l = l // 2
    #정사각형 내 숫자있는지 없는지 돌기 위한 좌표 리스트
    check_list = [(nx,ny), (nx, ny+l), (nx+l, ny), (nx+l, ny+l)]
    #정사각형 내 좌표 없을 때 board에 숫자 넣기 위한 좌표 리스트
    board_list = [(nx+(l-1), ny+(l-1)), (nx+(l-1), ny+l), (nx+l, ny+(l-1)), (nx+l, ny+l)]
    
    next_count = count
    for c, b in zip(check_list, board_list):
        #정사각형 내 숫자 없으면 board에 숫자 넣기
        if check(c[0], c[1], l) == 1:
            board[b[0]][b[1]] = count
        #l이 1이 아닐 때까지 divide반복
        if l != 1:
            next_count += 1
            divide(c[0], c[1], l, next_count)
        
divide(0,0,l,1)

for i in range(l):
    for j in range(l):
        print(board[i][j], end=' ')
    print()