N, K = map(int, input().split())
board = list(map(int, input().split()))
print(board)

#벨트가 각 칸위에 있는 로봇과 함께 한칸 회전
#이동하려는 칸에 로봇이 없거나, 내구도가 1이상이면 이동
#내구도 1이상이면 로봇 올림
#내구도가 0인 칸의 개수가 K개이상이면 종료