N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
move_list = [list(map(int, input().split())) for _ in range(M)]
dir = [[0,-1],[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]
clouds = [[N-2,0], [N-2,1], [N-1,0], [N-1,1]]

for move in move_list:
    visited = [[False for _ in range(N)] for _ in range(N)]
    # 이동
    d = dir[move[0]-1]
    t = move[1] % N

    for idx, cloud in enumerate(clouds):
        cloud[0] = cloud[0] + (d[0] * t)
        cloud[1] = cloud[1] + (d[1] * t)

        #시간 초과 원인!!!
        for c in range(2):
            if cloud[c] < 0:
                cloud[c] = N - (abs(cloud[c]) % N)
            elif cloud[c] >= N:
                cloud[c] = cloud[c] % N

        clouds[idx] = [cloud[0], cloud[1]]
        visited[cloud[0]][cloud[1]] = True

    #물채우기
    for idx, cloud in enumerate(clouds):
        board[cloud[0]][cloud[1]] += 1

    #대각선 물있는 구르 수 만큼 물채우기
    for idx, cloud in enumerate(clouds):
        count = 0
        for i in range(1,8,2):
            nx = cloud[0] + dir[i][0]
            ny = cloud[1] + dir[i][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] > 0:
                count += 1
        board[cloud[0]][cloud[1]] += count

    clouds = []
    #새로운 구름 만들기
    for x in range(N):
        for y in range(N):
            #시간 초과 원인!visited만들자
            if visited[x][y] == True:
                continue
            if board[x][y] >= 2:
                clouds.append([x, y])
                board[x][y] -= 2


print(sum(sum(l) for l in board))