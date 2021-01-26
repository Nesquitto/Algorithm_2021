answers = [1,3,2,4,2]

def solution(answers):
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thi = [3,3,1,1,2,2,4,4,5,5]
    sol = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == fir[i%5]:
            sol[0]+=1
        if answers[i] == sec[i%8]:
            sol[1]+=1
        if answers[i] == thi[i%10]:
            sol[2]+=1
    if sol[0]>= sol[1] and sol[0] >=sol[2]:
        answer.append(1)
    if sol[1]>= sol[0] and sol[1] >=sol[2]:
        answer.append(2)
    if sol[2]>= sol[0] and sol[2] >=sol[1]:
        answer.append(3)
    
    return answer

print(solution(answers))