numbers = 	[1000, 0, 5, 99, 100]

def solution(numbers):
    answer = ""
    dic = {'9': [], '8': [],'7': [],'6': [],'5': [],'4': [],'3': [],'2': [],'1': [],'0': []}
    for i in numbers:
        if str(i)[0] in dic:
            dic[str(i)[0]].append(str(i))
        else:
            dic[str(i)[0]].append(str(i))
    for i in dic.values(): # 각 리스트 9 8 7 ...0
        for j in range(len(i)):
            tmp = '0'
            le = 3
            for k in i:
                if int(tmp)*10**le < int(k)*10**(4-len(k)):
                    tmp, le = k, 4-len(k)
            answer += tmp
            i.remove(tmp)
    return answer
print(solution(numbers))