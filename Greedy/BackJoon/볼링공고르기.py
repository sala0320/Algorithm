N, M = map(int, input().split())
ball = list(map(int, input().split()))


def combi(arr, n):
    result = []
    if len(arr) < n:
        return result

    if n == 1:
        for a in arr:
            result.append([a])
    else:
        for i in range(len(arr) - n + 1):
            for temp in combi(arr[i + 1:], n - 1):
                if temp[0] != arr[i]:
                    result.append([arr[i]] + temp)
    return result


result = combi(ball, 2)
print(len(result))