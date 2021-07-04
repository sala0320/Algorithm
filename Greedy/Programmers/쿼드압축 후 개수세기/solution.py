def solution(arr):
    arr_len = len(arr)
    def quard(x,y,l):
        if l == 1:
            return [0,1] if arr[x][y] == 1 else [1,0]

        a = quard(x, y, l //2)
        b = quard(x, y + l//2, l //2)
        c = quard(x + l//2, y, l //2)
        d = quard(x + l//2, y + l//2, l //2)

        q_sum = list(map(sum, zip(a,b,c,d)))
        if q_sum == [4,0]:
            return [1,0]
        elif q_sum == [0,4]:
            return [0,1]
        else:
            return q_sum

    result = quard(0,0, arr_len)
    return result
