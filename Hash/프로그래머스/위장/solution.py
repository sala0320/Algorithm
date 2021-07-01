def solution(clothes):
    c_dict = dict()
    for n, c in clothes:
        c_dict[c] = c_dict.get(c, 0) + 1
    
    result = 1
    for v in c_dict.values():
        result *= (v + 1)
        
    return result - 1
