N = int(input())
#T, P
time_table = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for i in range(N+1)]

for t in range(N-1, -1, -1):
    if t + time_table[t][0] > N:
        if t + time_table[t][0] > N:
            dp[t] = dp[t+1]
    else:
        dp[it] = max(time_table[t][1] + dp[t + time_table[t][0]], dp[t+1])

print(dp[0])