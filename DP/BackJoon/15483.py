A = str(input())
B = str(input())
lenA = len(A)
lenB = len(B)
board = [[0 for _ in range(lenA + 1)] for _ in range(lenB + 1)]

for i in range(lenA + 1):
    board[0][i] = i
for j in range(lenB + 1):
    board[j][0] = j

for b in range(1, lenB + 1):
    for a in range(1, lenA + 1):
        if A[a - 1] == B[b - 1]:
            board[b][a] = board[b - 1][a - 1]
        else:
            board[b][a] = min(board[b - 1][a - 1], board[b][a - 1],
                              board[b - 1][a]) + 1
print(board[lenB][lenA])
