# 실패율 높은 순
def solution(N, stages):
    answer = []
    total = len(stages)
    for i in range(1, N + 1):
        count = 0
        for s in stages:
            if s == i:
                count += 1
        if total <= 0:
            answer.append([0, i])
        else:
            answer.append([count / total, i])
        total -= count

    answer.sort(key=lambda x: (-x[0], x[1]))
    for k, a in enumerate(answer):
        answer[k] = a[1]
    return answer