def check(string):
    s_stack = []
    for s in string:
        if len(s_stack) == 0:
            s_stack.append(s)
        elif (s == ')') and (s_stack[-1] == '('):
            s_stack.pop()
        elif (s == ']') and (s_stack[-1] == '['):
            s_stack.pop()
        elif (s == '}') and (s_stack[-1] == '{'):
            s_stack.pop()
        else:
            s_stack.append(s)

    if len(s_stack) == 0: 
        return True
    return False

def solution(s):
    count = 0
    string = list(s)
    str_len = len(string)
    new = []
    for i in range(str_len):
        new[:str_len-i] = string[i:]
        new[str_len-i:] = string[:i]
        if check(new):
            count += 1

    return count
