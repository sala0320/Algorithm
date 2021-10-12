#최소 몇번만에 빨간구슬을 구멍을 통해서 빼내는
#빨간 파랑 구슬 동시에 같은칸 안됨 파란구슬 구멍에 빠지면 실패 동시에 빠져도 실패
#왼쪽, 오른쪽, 위쪽, 아래쪽으로 기울이기 더이상 구슬이 움직일지 않을 때까지
#. 빈칸 # 장애물 벽 o 구멍의 위치 R 빨간 구슬의 위치 B 파란 구슬의 위치
from collections import deque
N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
visited = []


# R, B start 체크
queue = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
          rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j
queue.append((rx, ry, bx, by, 0))

#상하좌우 방향
direct = [[0,1], [0,-1], [-1, 0], [1, 0]]

#움직일 수 있는 만큼 움직이기
def move(x, y, d):
    c = 0
    #다음 칸이 벽이 아니고, 현재칸이 구멍이 아닐 때
    while(board[x+ d[0]][y+ d[1]] != '#' and board[x][y] != 'O'):
        x = x + d[0]
        y = y + d[1]
        c = c + 1
    #다음 칸이 벽이거나, 현재칸이 구멍일 때 좌표 반
    return x, y, c

#dfs실행
print(queue)
def dfs():
    while(queue):
        #queue에서 꺼내기
        rx, ry, bx, by, count = queue.popleft()
        visited.append((rx, ry, bx, by))

        #10번이상이면 -1 종료
        if count > 10:
            return -1

        #네방향 돌면서 다음 방향 체크
        for d in direct:
            nrx, nry, rc = move(rx, ry, d)
            nbx, nby, bc = move(bx, by, d)

            #빨, 파 같은 위치일때
            if nrx == nbx and nry == nby:
                if rc < bc:
                    nbx = nbx - d[0]
                    nby = nby - d[1]
                else:
                    nrx = nrx - d[0]
                    nry = nry - d[1]

            print(nrx, nry, nbx, nby)

            #파란색이 O에 빠졌을 때
            if board[nbx][nby] == 'O':
                continue

            #빨간색이 O에 빠졌을 때 종료
            if board[nrx][nry] == 'O' and board[nbx][nby] != 'O':
                count = count + 1
                return count

            #다 아니면
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, count+1))

        print(queue)
    return -1

print(dfs())