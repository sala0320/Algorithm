N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,1],[1,0],[0,-1], [-1,0]] #우하좌상


print(board)