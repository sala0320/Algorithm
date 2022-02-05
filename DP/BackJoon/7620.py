A = str(input())
B = str(input())
lenA = len(A)
lenB = len(B)
dp = [[0 for _ in range(lenA + 1)] for _ in range(lenB + 1)]
for a in range(lenA + 1):
    dp[0][a] = a
for b in range(lenB + 1):
    dp[b][0] = b
for i in range(1, lenB + 1):
    for j in range(1, lenA + 1):
        if A[j - 1] == B[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
print(dp)
x, y = lenB, lenA
while (x >= 0 and y >= 0):
    # print(x, y)
    min_num = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y])
    if min_num == dp[x][y - 1]:
        print('d', B[x - 1])
        x, y = x, y - 1
    elif min_num == dp[x - 1][y]:
        print('a', B[x - 1])
        x, y = x - 1, y
    elif dp[x][y] == dp[x - 1][y - 1]:
        print('c', B[x - 1])
        x, y = x - 1, y - 1
    elif min_num == dp[x - 1][y - 1]:
        print('m', B[x - 1])
        x, y = x - 1, y - 1
