def solution(participant, completion):
    dictionary = dict()
    for i in completion:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    for i in participant:
        if i in dictionary:
            if dictionary[i] > 0:
                dictionary[i] = dictionary[i] - 1
            else:
                answer = i
                break
        else:
            answer = i
            break
    return answer