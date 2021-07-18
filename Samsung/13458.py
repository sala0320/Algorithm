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
        
