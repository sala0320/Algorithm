N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))
for i, t in enumerate(triangle[1:]):
    i += 1
    for j in range(len(t)):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(t)-1:
            triangle[i][j] += triangle[i-1][len(triangle[i-1])-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
print(max(triangle[-1]))