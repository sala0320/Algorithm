#visited 수정
#queue에 넣는 수 수정
from collections import deque
dir = [(0,1), (1,0), (-1,0), (0,-1)]
def bfs(board, N):
    queue = deque([[(0,0), (0,1), 0, 0]])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while(queue):
        l, r, c, v = queue.popleft()
        # print(l, r, c, v)
        # print(visited)
        # print(queue)
        if r[0] == N-1 and r[1] == N-1 and r[0] == N-1 and r[1] == N-1::
            return c
        
        for d in dir:
            nl = tuple(sum(z) for z in zip(l, d))
            nr = tuple(sum(z) for z in zip(r, d))
            if nl[0] < 0 or nl[1] < 0 or nr[0] < 0 or nr[1] < 0 or nl[0] >= N or nl[1] >= N or nr[0] >= N or nr[1] >= N:
                    continue
            if board[nl[0]][nl[1]] == 1 or board[nr[0]][nr[1]] == 1:
                continue
            # if visited[nl[0]][nl[1]] == 0:
                # visited[nl[0]][nl[1]] = 1      
            queue.append([nl, nr, c+1, v])
                
        turn_list = [l, r]
        for t in turn_list:
            if v == 0:
                turn_dir = [(-1,0), (1,0)]
            else:
                turn_dir = [(0,-1), (0,1)]
                
            for d in turn_dir:
                tl = t
                tr = tuple(sum(z) for z in zip(t, d))
                if tl[0] < 0 or tl[1] < 0 or tr[0] < 0 or tr[1] < 0 or tl[0] >= N or tl[1] >= N or tr[0] >= N or tr[1] >= N:
                        continue
                if board[tl[0]][tl[1]] == 1 or board[tr[0]][tr[1]] == 1:
                    continue
                # if visited[tl[0]][tl[1]] == 0:
                    # visited[tl[0]][tl[1]] = 1          
                queue.append([tl, tr, c+1, (v+1)%2])
            
def solution(board):
    answer = bfs(board, len(board))
    return answer