N, M = map(int, input().split())
bridge = [list(map(int, input().split())) for _ in range(M)]
s, d = map(int, input().split())

board = [[0 for _ in range(N)] for _ in range(N)]
for b in bridge:
    board[b[0]-1][b[1]-1] = max(b[2], board[b[0]-1][b[1]-1])
    board[b[1]-1][b[0]-1] = max(b[2], board[b[1]-1][b[0]-1])
print(board)

    
