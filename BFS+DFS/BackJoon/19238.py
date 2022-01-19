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
N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())
destination = []
for m in range(1, M+1):
    info = list(map(int, input().split()))
    board[info[0]-1][info[1]-1] = -m
    destination.append((info[2]-1, info[3]-1))

def find_passenger(x,y,f,c):
    return

def find_destination(x,y,f,c):
    return

for _ in range(M):
    X, Y, F, C = find_passenger(X,Y,F,0)
    if X == -1:
        print(-1)
        break
    else:
        X, Y, F, C = find_destination(X,Y,F,0)
        if X == -1:
            print(-1)
            break