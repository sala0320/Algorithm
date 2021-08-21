from sys import stdin, stdout

N = int(stdin.readline())
check = [0] * 10001
#반복되는 수 많고(수 크기 제한은 작으나 개수 제한은 큼) 
#메모리 초과나므로 기수정렬 사용
for _ in range(N):
    n = int(stdin.readline())
    check[n] = check[n] + 1
    
for i, c in enumerate(check):
    if c != 0:
        for _ in range(c):
            stdout.write(str(i) + '\n')

    