#https://www.acmicpc.net/problem/11053
N = int(input())
num = list(map(int, input().split()))
dp = [1] * (N+1)
for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))