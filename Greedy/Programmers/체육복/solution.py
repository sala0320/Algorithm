def solution(n, lost, reserve):
    lost = sorted(lost)
    resrve = sorted(reserve)

    same = list(set(lost).intersection(set(reserve)))
    count = n - len(lost) + len(same)
    
    for s in same:
        lost.remove(s)
        reserve.remove(s)
    
    for l in lost:  
        if reserve.count(l+1) > 0:
            reserve.remove(l+1)  
            count = count + 1
            
        elif reserve.count(l-1) > 0:
            reserve.remove(l-1)      
            count = count + 1
            
    return count
