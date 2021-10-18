# N개의 수 N-1개의 연산자 +,-,x,/
# 만들 수 있는 식의 결과가 최소인것과 최대인것을 고르기
# 연산자 우선순위 무시하고 계산, 음수 / 양수 = 양수로 바꿈 / 양수 -> 몫 음수
N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

def dfs(idx, total, plus, minus, mul, div):
    global Min, Max
    if idx == N:
        Max = max(total, Max)
        Min = min(total, Min)
        return

    if plus:
        dfs(idx+1, total + A[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, total - A[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, total * A[idx], plus, minus, mul-1, div)
    if div:
        dfs(idx+1, int(total / A[idx]), plus, minus, mul, div-1)

Min = 1e9
Max = -1e9
dfs(1, A[0], C[0], C[1], C[2], C[3])

print(Max)
print(Min)
'''
#--------시간초과---------#
(4,0,0,0) 1+2+3+4+5 5번만 함수를 수행하면 되는데, +위치를 계속 바꿔가면서 여러번 수행하게 됨
for i, op in enumerate(operator):
    if visited[i] == 1:
        continue

    visited[i] = 1
    list.append(op)
    dfs(idx + 1, list)
    visited[i] = 0
    list.pop()
'''