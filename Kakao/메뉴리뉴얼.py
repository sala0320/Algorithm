#combinations
#Counter

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for c in course:
        order_list = []
        for o in orders:
            if len(o) < c:
                continue
            order_list.extend(list(map(''.join, combinations(sorted(o),c))))
            #XY = YX이여햐 하므로 sorted(o)한 후 combi하기!!
            
        order_count = Counter(order_list).most_common()
        if len(order_count) > 0:
            max_count = int(order_count[0][1])
            if max_count == 1:
                break
            for oc in order_count:
                if int(oc[1]) < max_count:
                    break
                answer.append(oc[0])
            
    return sorted(answer)