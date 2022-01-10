A = int(input())
num = list(map(int, input().split()))
dp = [0] * A
dp[0] = num[0]
count = 1
if A >= 1:
    for i in range(2, A):
        if num[i] >= num[i-1]:
            dp[i] = num[i]
        elif num[i] < num[i-1]:
            dp[i] = num[i-1]
            count += 1
print(count)
