# N : 시험장
# Ai : 응시자 수
# B(1명) : 총 감족관이 한시험장에서 감시할 수 있는 응시자 수
# C(여러명) : 부감독관이 한시험장에서 감시할 수 있는 응시자 수
# 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수를 출력
# (Ai - B)/c
import math

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

result = 0;
for stu in S:
    temp = stu - T[0]
    if (temp > 0):
        result += (math.ceil(temp / T[1]) + 1)
    else:
        result += 1
print(result)
        
