def solution(phone_book):
    for i in phone_book:
        phone_book.remove(i)
        for j in phone_book:
            if len(i) < len(j):
                if i == j[0:len(i)]:
                    return False
            else:
                if i[0:len(j)] == j:
                    return False
    return True