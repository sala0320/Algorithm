N = int(input())
time_price = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]
for i in range(N-1, -1, -1):

    if i + time_price[i][0] <= N:
        dp[i] = max(dp[i+1], time_price[i][1] + dp[i + time_price[i][0]])
    else:
        dp[i] = dp[i+1]
print(dp[0])