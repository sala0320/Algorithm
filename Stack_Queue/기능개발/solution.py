import math
def solution(progresses, speeds):
    count_array = []
    result = []
    count = 0

    for i,(p,s) in enumerate(zip(progresses, speeds)):
        last = math.ceil((100 - p) / s) 
        if i == 0:
            current = last
            count_array.append(last)
        else:    
            if current < last:
                current = last
                print(count_array)
                while count_array:
                    count_array.pop()
                    count += 1

                result.append(count)
                count = 0
                count_array.append(last)
            else:
                count_array.append(last)

    result.append(len(count_array))

    return result
