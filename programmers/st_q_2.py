import math
def solution(progresses, speeds):
    a = 0
    li = []
    sec = 0
    while(len(progresses) != 0):
        if(progresses[0]+speeds[0]*sec >=100):
            a +=1
            del progresses[0]
            del speeds[0]
        else:
            if(a !=0):
                li.append(a)
                a = 0
            sec = math.ceil((100-progresses[0])/speeds[0])
    li.append(a)
    return li