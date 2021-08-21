#숫자카드 N개 given 정수 M개
from sys import stdin, stdout

stdin.readline()
N_list = set(map(int, stdin.readline().split()))
print(N_list)

stdin.readline()
M_list = list(map(int, stdin.readline().split()))

for m in M_list:
    if m in N_list:   
        stdout.write('1 ')
    else:
        stdout.write('0 ')

