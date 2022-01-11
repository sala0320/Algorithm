#https://www.acmicpc.net/problem/11722
A = int(input())
num = list(map(int, input().split()))
#dp = i까지 감소하는 수들의 개수
#7 5 8 2 10 -> [1 2 1 3 1]
dp = [1] * A
for i in range(A):
    for j in range(i):
        #이전 수 > 현재 수
        if num[j] > num[i]:
            # max(현재까지의 감소하는 수 개수, 이전 수까지의 감소하는 수 개수)
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))