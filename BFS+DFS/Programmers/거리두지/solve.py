from collections import deque
direction = [[1,0], [0,1], [0,-1], [-1,0]]
def check(arr):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                visited = [[0 for _ in range(5)] for _ in range(5)]
                queue = deque([[i,j,0]])
                visited[i][j] = 1

                while(queue):
                    x, y, t = queue.popleft()

                    for d in direction:
                        nx = x + d[0]
                        ny = y + d[1]
                        nt = t + 1

                        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[nx][ny] == 1:
                            continue
                        if arr[nx][ny] == 'P':
                            return 0
                        if arr[nx][ny] == 'O' and nt < 2:
                            queue.append([nx,ny,nt])
                            visited[nx][ny] = 1
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer
