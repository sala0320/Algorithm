N, M = map(int, input().split())
result = []
visited = [0]*(N)
def dfs(depth):
    if depth == M:
        for i in range(len(result)):
            print(result[i]+1, end=" ")
        print()
        return

    for num in range(N):
        if not visited[num]:
            visited[num] = 1
            result.append(num)
            dfs(depth+1)
            visited[num] = 0
            result.pop()
dfs(0)