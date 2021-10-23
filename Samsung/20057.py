
def check(time, type, dir):
    global s_x, s_y, result
    for _ in range(time):
        s_x += dir[0]
        s_y += dir[1]
        if s_y < 0:
            break

        total = 0
        for dx,dy,z in type:
            nx = s_x + dx
            ny = s_y + dy
            #a일때
            if z == 0:
                new = board[s_x][s_y] - total
            else:
                new = int(board[s_x][s_y] * z)
                total += new

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                result += new
            else:
                board[nx][ny] += new

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
#방향별 모래 비율 위치
dir = [(0,-1),(1,0), (0,1), (-1,0)]
left = [(-1,1,0.01),(1,1,0.01),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),
        (-1,-1,0.1),(1,-1,0.1),(0,-2,0.05), (0,-1,0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

s_x, s_y = N//2, N//2
result = 0

for i in range(1, N+1):
    if i % 2:
        check(i, left, dir[0])
        check(i, down, dir[1])

    else:
        check(i, right, dir[2])
        check(i, up, dir[3])

print(result)