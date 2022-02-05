N = int(input())
board = [tuple(map(int, input().split())) for _ in range(N)]
board.sort(key=lambda x: (x[0], x[1]))
for b in board:
    print(b[0], b[1])