#if-elif로 하면 2,3으로 둘다 나누어 지는 경우 잡지 못함
N = int(input())
dp = [0] * (N + 1)
if N >= 2:
    dp[2] = 1

#Bottom-Up
# for i in range(3, N + 1):
# dp[i] = min(dp[i // 2] + (i % 2), dp[i // 3] + (i % 3)) + 1


# Top-down
def td(n):
    if n <= 2:
        return dp[n]
    dp[n] = min(td(n // 3) + (n % 3), td(n // 2) + (n % 2)) + 1
    return dp[n]


td(N)
print(dp)
print(dp[N])