a, b, c = map(int, input().split())
count = 0
while True:
    # print(a, b, c)
    if b - a == 1 and c - b == 1:
        print(count)
        break
    if b - a < c - b:
        a = b
        b = b + 1
    else:
        c = b
        b = b - 1
    count += 1
