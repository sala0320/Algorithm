#(학생, 게시시간, 추천수)로 해보기

from collections import deque

N = int(input())
R = int(input())
student = list(map(int, input().split()))
queue = deque([(student[0], 0)])
student.pop(0)


def check(list, s):
    for l in list:
        if l[0] == s:
            return l, l[1]
    return list[-1], -1


def change(list, dup, dup_count, s):
    flag = 0
    # print(list, dup)
    for i, l in enumerate(list):
        if l[1] <= dup[1] + 1:
            # print(i, s)
            list.insert(i, (s, dup_count + 1))
            flag = 1
            break
    if flag == 0:
        list.append((s, dup_count + 1))

    return list


for s in student:
    dup, dup_count = check(queue, s)
    # print(dup, dup_count)
    # print(s)
    length = len(queue)
    if dup_count == -1:
        if length == N:
            queue.remove(dup)
    else:
        queue.remove(dup)

    queue = change(queue, dup, dup_count, s)
    # print(queue)
queue = list(queue)
queue.sort(key=lambda x: x[0])
for q in queue:
    print(q[0], end=" ")
