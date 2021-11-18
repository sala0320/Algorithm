import re
def solution(new_id):
    new_id = new_id.lower()
    #new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)
    #new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = re.sub(r"\.{2,}",".",new_id)
    #new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = re.sub(r"^\.","",new_id)
    new_id = re.sub(r"\.$","",new_id)
    
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) > 15:
        new_id = new_id[:15]
    new_id = re.sub(r"\.$","",new_id)
    if len(new_id) < 3:
        l = new_id[-1]
        while(len(new_id) != 3):
            new_id += l
    
    print(new_id)
    return new_id