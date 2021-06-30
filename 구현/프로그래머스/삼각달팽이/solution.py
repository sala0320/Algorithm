from itertools import chain
def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]

    x,y = -1, 0
    num = 1

    for i in range(n):
        for j in range(n-i):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            maps[x][y] = num
            num += 1
    result = [i for i in chain(*maps) if i != 0]
    return result
