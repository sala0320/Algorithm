N = int(input())
score = [list(map(str, input().split())) for _ in range(N)]
for i, s in enumerate(score):
    score[i] = [s[0], int(s[1]), int(s[2]), int(s[3])]
score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in score:
    print(s[0])