from sys import stdin, stdout
from bisect import bisect

N = int(stdin.readline())
N_list = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))
N_list.sort()

def binary_search(m):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2

        if N_list[mid] == m:
            return 1
        elif N_list[mid] > m:
            right =  mid - 1
        else:
            left = mid + 1
    return 0

for m in M_list:
    if binary_search(m):
        stdout.write('1\n')
    else:
        stdout.write('0\n')



# for m in M_list:
#     if bisect(N_list, m) == m:
#         stdout.write('1\n')
#     else:
#         stdout.write('0\n')