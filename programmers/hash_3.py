def solution(clothes):
    answer = 1
    dictionary  = dict()
    for i in clothes:
        if i[1] in dictionary:
            dictionary[i[1]] = dictionary[i[1]] + 1
        else:
            dictionary[i[1]] = 1
    for i in dictionary.values():
        answer = answer * (i+1)
    return answer-1
