#플로이드 와샬
def solution(n, s, a, b, fares):
    board = [[1e9] * n for _ in range(n)]
    #board자기자신 0으로 초기화
    for n_ in range(n):
        board[n_][n_] = 0
    
    #board[i][j] = board[j][i] = c i~j까지의 cost
    for f in fares:
        board[f[0]-1][f[1]-1] = board[f[1]-1][f[0]-1] = f[2]
    
    #board업데이트 min(바로가는거, 들렸다가는거)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
 
    result = 1e9
    s,a,b = s-1,a-1,b-1
    #min(result, min(각각 따로 바로가는거, 중간에서 각각 따로 가는거))
    for n_ in range(n):
        result = min(result, min(board[s][a] + board[s][b], board[s][n_] + board[n_][a] + board[n_][b]))
    return result