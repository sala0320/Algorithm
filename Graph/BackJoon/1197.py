N, M = int(input()), int(input())
cost = [list(map(int, input().split())) for i in range(M)]
#세번째 값 기준으로 sort
cost.sort(key=lambda x : x[2])
