import re
def solution(s):

    num_dict = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
                'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for d in num_dict.items():
        s = re.sub(d[0], d[1], s)
    return int(s)