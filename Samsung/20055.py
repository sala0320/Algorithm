from collections import deque
N, K = map(int, input().split())
queue = deque(list(map(int, input().split())))
robot = deque(list([0] * N))

result = 1
while True:
    # 1단계 벨트가 한 칸 회전한다.
    queue.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2단계 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 만약 이동할 수 없다면 가만히 있는다.
    for i in range(-2, -N-1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and queue[i + 1 - N] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            queue[i + 1 - N] -= 1
    robot[-1] = 0

    # 3단계 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and queue[0] > 0:
        robot[0] = 1
        queue[0] -= 1

    # 4단계
    if queue.count(0) >= K:
        break
    result += 1
print(result)