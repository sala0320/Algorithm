# NxM (r,c) = (북쪽으로부터 떨어진 칸의 개수, 서쪽으로 부터 떨어진 칸의 개수)
# d (북,동,남,서)
# 1. 현재 위치 청소
# 2. 왼쪽부터 인접한 칸 탐색
#    청소 X : 그 방향으로 회전한 후 한칸 이동 후 1번으로
#    청소 O : 그 방향으로 회전한 후 2번으로
#    네 방향 모두 청소 O, 벽 : 바라보는 방향을 유지한 채 한 칸 후진한 후 2번으로
#    네 방향 모두 청소 O, 벽, 뒤쪽 방향도 벽 : 작동을 멈춤
# 주의 할 점 : 재귀로 풀면 python3타임아웃!
dir = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
R, C, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def clean_board(x, y, d, clean, count):
    while(1):
        visited[x][y] = 1
        #종료 조건
        if count == 4:
            back_dir = (d + 2) % 4
            dx = x + dir[back_dir][0]
            dy = y + dir[back_dir][1]
            #뒤에 벽있으면 끝
            if(board[dx][dy]) == 1:
                print(clean)
                break
            #뒤에 벽 없으면 뒤로
            else:
                x = dx
                y = dy
                count = 0
        
        #왼쪽 인접칸 탐색
        new_dir = (d - 1) % 4
        nx = x + dir[new_dir][0]
        ny = y + dir[new_dir][1]

        #왼쪽 인접칸 청소O OR 벽 O
        if (visited[nx][ny] == 1) or (board[nx][ny] == 1):
            d = new_dir
            count += 1
        #왼쪽 인접칸 청소 X + 벽 X
        else:
            x = nx
            y = ny
            d = new_dir
            clean += 1
            count = 0

clean_board(R, C, D, 1, 0)