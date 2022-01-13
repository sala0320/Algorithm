#if-elif로 하면 2,3으로 둘다 나누어 지는 경우 잡지 못함
N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp)