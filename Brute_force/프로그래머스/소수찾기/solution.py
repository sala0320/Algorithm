from itertools import permutations
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def solution(numbers):
    answer = []
    num_len = len(numbers)
    num_list = list(numbers)
    num = []    
    for i in range(1,num_len+1):
        for n in list(map(''.join, permutations(num_list,i))):
            if (is_prime(int(n)) == True) and (int(n) > 1):           
                answer.append(int(n))
    return len(set(answer))
