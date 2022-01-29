N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
Min = 1e9
Max = -1e9

def dfs(idx, total, plus, minus, mul, div):
    global Min, Max
    if idx == N:
        Max = max(total, Max)
        Min = min(total, Min)
        return

    if plus:
        dfs(idx + 1, total + A[idx], plus - 1, minus, mul, div)
    if minus:
        dfs(idx + 1, total - A[idx], plus, minus - 1, mul, div)
    if mul:
        dfs(idx + 1, total * A[idx], plus, minus, mul - 1, div)
    if div:
        # dfs(idx + 1, total // A[idx], plus, minus, mul, div - 1)
        dfs(idx + 1, int(total / A[idx]), plus, minus, mul, div - 1)


dfs(1, A[0], C[0], C[1], C[2], C[3])
print(Max)
print(Min)