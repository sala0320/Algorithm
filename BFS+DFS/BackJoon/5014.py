from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)

def dfs(start):
    queue = deque([])
    queue.append((start, 0))
    while(queue):
        n, c = queue.popleft()
        visited[n] = 1
        # print(n, c)
        if n == G:
            return c
        else:
            if n+U <= F and visited[n+U]==0:
                visited[n+U] = 1
                queue.append((n + U, c + 1))
            if n-D > 0 and visited[n-D]==0:
                visited[n-D] = 1
                queue.append((n - D, c + 1))
    return -1

result = dfs(S)
if result == -1:
    print("use the stairs")
else:
    print(result)

