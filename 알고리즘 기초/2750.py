from collections import deque
N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()
for n in num_list:
    print(n)