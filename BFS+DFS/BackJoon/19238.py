# 연료 바닥나면 끝남
# 현재위치에서 최단 거리 짧은 고개 -> 행 번호 작은 승객 -> 열 번호 작은 승객
# 목적지 도착하면 소모한 연료양의 두배 충전 
# 첫시도 : 도착지까지 가는 거리를 도착지 (x,y)에서 현재 (x,y)를 뻄 -> 중간에 벽 있을 수도 있어서 안됨 / bfs 두개로 하기
from collections import deque
import sys
input = sys.stdin.readline
N, M, S = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
destination = []
dir = [[1,0], [0,1], [-1,0], [0,-1]]
#board에 손님 있는 칸에 손님 출발지번호(2), 도착지번호(-2) 입력
for i in range(M):
    customer = list(map(int, input().split()))
    board[customer[0]-1][customer[1]-1] = i+2
    board[customer[2]-1][customer[3]-1] = -(i+2)
print(board)
#가장 가까운 승객 찾는 bfs
#시작 위치, 현재 남은 연료, 현재까지 이동한 수
def find_bfs(sx, sy, sf, sc):
    #덱에 시작위치 입력
    queue = deque([])
    queue.append((sx, sy, sf, sc))
    #visited 배열 설정
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = 1
    #같은 최소거리일때를 위헤 최소거리 승객들 위치 저장할 배열
    passenger = []
    min_cost = 1e9
    print("FIND")
    print(sx, sy, sf, sc)

    while(queue):
        x, y, f, c = queue.popleft()
        nf = f-1
        nc = c+1
        #현재까지 이동한 거리가 최단거리보다 길면 종료
        if nc > min_cost:
            break 
        if nf < 0:
            return -1
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1 or visited[nx][ny] == 1:
                continue
            #현재 board위치에 사람이 있으면
            if board[nx][ny] > 1:
                #승객 현재 위치, 승객 번호, 남은 연료
                passenger.append((nx, ny, board[nx][ny], nf))
                min_cost = c+1
                
            #현재 board위치가 지나갈 수 있는 길이면
            else:
                visited[nx][ny] = 1
                queue.append((nx, ny, nf, nc))

    passenger.sort(key=lambda x : (x[0], x[1]))
    board[passenger[0][0]][passenger[0][1]] = 0
    return (passenger[0])

#최단거리로 목적지까지 가는 dfs
#승객 현재 위치, 승객 번호, 남은 연료
def dest_dfs(dx, dy, dn, df, dc):
    print("DEST")
    print(dx,dy,dn,df,dc)
    queue = deque()
    queue.append((dx, dy, dn, df, dc))

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[dx][dy] = 1
    
    while(queue):
        x, y, n, f, c = queue.popleft()

        if f == 0:
            return -1
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            nf = f - 1
            nc = c + 1
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1 or visited[nx][ny] == 1:
                continue
            if board[nx][ny] == n:
                nf = nf + (nc * 2) 
                return (nx, ny, nf)
            else:
                visited[nx][ny] = 1
                queue.append((nx, ny, n, nf, nc))


startx = start[0]-1
starty = start[1]-1
startc = S
for _ in range(M):
    print("START")
    find_result = find_bfs(startx, starty, startc, 0)
    print(find_result)
    if find_result == -1:
        print("-1")
        break
    else:
        dest_result = dest_dfs(find_result[0], find_result[1], -find_result[2], find_result[3], 0)
        print(dest_result)
        if dest_result == -1:
            print("-1")
            break
        else:
            startx = dest_result[0]
            starty = dest_result[1]
            startc = dest_result[2]

print(startc)


