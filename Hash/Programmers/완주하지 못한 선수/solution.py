from collections import Counter
def solution(participant, completion):
    return list((Counter(participant)-Counter(completion)).keys())[0]
    # participant.sort()
    # completion.sort()
    # for i in range(len(completion)):
    #     if completion[i] != participant[i]:
    #         return participant[i]
    # return participant[-1]
