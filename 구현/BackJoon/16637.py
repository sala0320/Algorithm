#괄호추가하기
#N 1일때 주의, MAX 초기값 -2^31주의
def calc(num1, num2, op):
    num1, num2 = int(num1), int(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2

def solve(idx, cal):
    global result, exp, N
    if idx > N-1:
        result = max(result, cal)
        return
    if idx + 2 < N:
        par = calc(cal, calc(exp[idx+1], exp[idx+3], exp[idx+2]), exp[idx])
        solve(idx+4, par)
    if idx < N:
        nopar = calc(cal, exp[idx+1], exp[idx])
        solve(idx+2, nopar)

result = -2 ** 31
N = int(input())
exp = str(input())
if N == 1:
    result = exp[0]
else:
    solve(1, exp[0])
print(result)