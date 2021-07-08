
import sys
from collections import deque
#입력받기
dx = [-1,1,0,0]
dy = [0,0,-1,1]
input = sys.stdin.readline
X, Y = map(int, input().split())
map = []
for _ in range(X):
    map.append(list(input().rstrip()))

visited  = [[0] * Y for _ in range(X)]
water_q = deque()
gosum_q = deque()


#map만들기
for i in range(X):
    for j in range(Y):
        if map[i][j] == "D":
            goal = [i, j]
        elif map[i][j] == "S":
            map[i][j] = "."
            gosum_q.append([i,j])
            visited[i][j] = 1
        elif map[i][j] == "*":
            map[i][j] = 0
            water_q.append([i,j])
        elif map[i][j] == "X":
            visited[i][j] = 1
           
# 물 이동
while water_q:
    x, y, cnt = water_q.popleft()
    for i,j in zip(dx, dy):
        nx = x + i
        ny = y + j
        if (0 <= nx < X) and (0 <= ny < Y) and (map[nx][ny] == "."):
            map[nx][ny] = cnt + 1
            water_q.append([nx, ny, cnt+1])
#고슴도치 이동
result = 0
while gosum_q:
    x,y,cnt = gosum_q.popleft()
    if [x,y] == goal:
        result = 1
        break
    for i,j in zip(dx,dy):
        nx = x + i
        ny = y + j
        if (0 <= nx < X) and (0 <= ny < Y) and (visited[nx][ny] == 0):
            if (map[nx][ny] == ".") or (map[nx][ny] > cnt + 1):
                print(nx, ny, cnt)
                visited[nx][ny] = 1
                gosum_q.append([nx, ny, cnt+1])

print(map)
print(visited)

if result == 0:
    print("KAKTUS")
else:
    print(cnt)