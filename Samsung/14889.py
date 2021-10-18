#짝수 N명
#Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치
#팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합
#두 팀의 차이를 최소출력

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
result = 1e9
def dfs(num, start, depth):
    global result
    if depth == num:
        start, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    start = start + S[i][j] + S[j][i]
                elif not visited[i] and not visited[j]:
                    link = link + S[i][j] + S[j][i]
        result = min(result, abs(start - link))

    for i in range(start, N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(num, i+1, depth+1)
        visited[i] = 0

dfs(N//2, 0, 0)
print(result)