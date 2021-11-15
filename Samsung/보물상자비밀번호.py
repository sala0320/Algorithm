from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = deque(list(str(input())))
    num_list = []
    side = N//4
    for _ in range(side):
        for i in range(4):
            n = ''.join(num[i*(side) : (i+1)*(side)])
            num_list.append(int(''.join(num[i*(side) : (i+1)*(side)]), 16))

        num.rotate(1)

    result = sorted(list(set(num_list)), reverse=True)
    print('#' + str(test_case) + ' ' + str(result[K-1]))
