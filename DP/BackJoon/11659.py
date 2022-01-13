import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
dp = [0] * (N+1)
for idx, num in enumerate(num_list):
    dp[idx+1] = dp[idx] + num
for _ in range(M):
    s, f = map(int, input().split())
    print(dp[f]-dp[s-1])

