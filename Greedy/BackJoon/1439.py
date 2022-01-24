string = str(input())


def check(string, char):
    now_count = 0
    count = 0
    for s in string:
        if s == char:
            if now_count == 0:
                count += 1
            now_count += 1
        else:
            now_count = 0

    return count


print(min(check(string, '0'), check(string, '1')))