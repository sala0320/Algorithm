def solution(answers):
    answer = []
    student = [[1, 2, 3, 4, 5]*2000, [2, 1, 2, 3, 2, 4, 2, 5]*1250,[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000]
    score = []
    for s in student:
        score.append(len([i for i,j in zip(s, answers) if i == j]))
    1
    max_s = max(score)
    answer = [i+1 for i,s in enumerate(score) if s == max_s] 
    return answer
