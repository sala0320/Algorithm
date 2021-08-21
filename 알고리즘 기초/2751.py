from sys import stdin, stdout

N = int(stdin.readline())
num_list = [int(stdin.readline()) for _ in range(N)]
num_list.sort()
for n in num_list:
    stdout.write(str(n) + '\n')
    