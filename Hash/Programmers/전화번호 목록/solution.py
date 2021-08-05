def solution(phone_book):
    phone_book.sort()
    phone_len = len(phone_book)
    for i in range(phone_len - 1):
        if(phone_book[i] != phone_book[i+1]) and (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            return False
    return True
