#Combination
#Dict
#Binary Search
from bisect import bisect_left
from itertools import combinations
def solution(info, query):
    answer = []
        
    cases = {}
    for i in info:
        info_list = i.split(' ')
        for c in range(5):
            for cb in combinations([0,1,2,3], c):
                case = ''
                for idx in range(4):
                    if idx in cb:
                        case += '-'
                    else:
                        case += info_list[idx]
                if case in cases.keys():
                    cases[case].append(int(info_list[4]))
                else:
                    cases[case] = [int(info_list[4])]

            for key in cases.keys():   
                cases[key].sort()

    for qu in query:
        qu_list = qu.split(' ')
        qu_case = qu_list[0] + qu_list[2] + qu_list[4] + qu_list[6]
        qu_score = qu_list[7]
        if qu_case in cases.keys():
            answer.append(len(cases[qu_case]) - bisect_left(cases[qu_case], int(qu_score), lo=0, hi=len(cases[qu_case])))
        else:
            answer.append(0)
    return answer