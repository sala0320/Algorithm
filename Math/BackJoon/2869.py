import math
A, B, V = map(int, input().split())
#(A-B) * N + A > V
print(math.ceil((V-A) / (A-B)) + 1)

#시간초과 코드
# count = 0
# now = 0
# while(1):
#     print(now)
#     now += A
#     if now < V:
#         now -= B
#         count += 1
#     else:
#         break
# print(count+1)