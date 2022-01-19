"""
NxN board M passenger
board(승객 있는 곳에 -숫자로 표사), visited(bfs할때 이미 지나간 길), department(도착지 좌표 정보)
1. 최단거리 승객 찾기
    - bfs queue(x, y, 남은 연료, 움직인 거리)
    - 같은 거리의 승객 행 작은, 열 작은 순 : 승객 만나면 heapq에 넣기
2. 도착지 최단거리 찾기
    - bfs queue(x, y, 남은 연료, 움직인 거리)
    - 도착지 만나면 남은 연료 += 움직인 거리 * 2
"""
from collections import deque
import heapq
from socket import AI_PASSIVE
N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())
destination = []

for m in range(1, M+1):
    info = list(map(int, input().split()))
    board[info[0]-1][info[1]-1] = -m
    destination.append((info[2]-1, info[3]-1))

dir = [(0,1), (1,0), (-1,0), (0,-1)]

def find_passenger(px,py,pf,pc):
    
    queue = deque([(px, py, pf, pc)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[px][py] = 1
    min_c = 1e9
    passenger = []

    while(queue):
        x, y, f, c = queue.popleft()
        if c > min_c:
            break

        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 0 and board[nx][ny] != 1 and f > 0:
                if board[nx][ny] < 0:
                    min_c = c
                    passenger.append((nx, ny, f-1, c+1))

                visited[nx][ny] = 1
                queue.append((nx, ny, f-1, c+1))
    
    if len(passenger) == 0:
        return -1,-1,-1,-1 
    passenger.sort()
    print(passenger)
    return passenger[0][0], passenger[0][1], passenger[0][2], passenger[0][3]

def find_destination(dx,dy,df,dc):

    queue = deque([(dx, dy, df, dc)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[dx][dy] = 1
    passenger_num = (-board[dx][dy]) - 1
    board[dx][dy] = 0

    while(queue):
        x, y, f, c = queue.popleft()
        if x == destination[passenger_num][0] and y == destination[passenger_num][1]:
            return x, y, f + (2 * c), c
    
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]    
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 0 and board[nx][ny] != 1 and f > 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, f-1, c+1))

    return -1, -1, -1, -1

NX, NY, NF = X-1, Y-1, F
for _ in range(M):
    NX, NY, NF, NC = find_passenger(NX,NY,NF,0)
    if NX == -1:
        result = -1
        break
    else:
        NX, NY, NF, NC = find_destination(NX,NY,NF,0)
        if NX == -1:
            result = -1
            break
        result = NF

if result == -1:
    print(result)
else:
    print(result)