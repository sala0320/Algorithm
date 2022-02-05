from collections import deque

N = int(input())
R = int(input())
student = list(map(int, input().split()))

pic = []
time = 1
for t, s in enumerate(student):
    flag = 0
    #pic에 이미 추천된 사람이 있는 경우 추천수만 증가
    for p in pic:
        if p[0] == s:
            p[1] += 1
            flag = 1
    #pic에 이미 추천된 사람이 없는 경우
    if flag == 0:
        #pic가 꽉 차있다면 우선순위 가장 낮은 것 제거
        if len(pic) == N:
            pic.pop()
        #(학생, 추천수, 게시시간)추가
        pic.append([s, 1, t])
    #추천순 많고, 게시시간 큰(가장 최근)순으로 정렬
    pic.sort(key=lambda x: (-x[1], -x[2]))

pic.sort(key=lambda x: x[0])
for p in pic:
    print(p[0], end=" ")
