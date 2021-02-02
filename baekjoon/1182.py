import sys

N, S  = map(int, sys.stdin.readline().split())
info = list(map(int, sys.stdin.readline().split()))
res = 0
sum = 0

def back(nextindex, sum):
    global info
    global res
    sum += info[nextindex]
    if(sum == S):
        res +=1
    else:
        for i in range(nextindex+1, len(info)):
            back(i, sum)

for i in range(0, len(info)):
    back(i, sum)
print(res)