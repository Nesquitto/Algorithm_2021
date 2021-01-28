import sys
pushnum = 0 # push해야하는 수
num = 0 # 스택의 마지막 수
li = [] # 스택

ll = []
res = True
for i in range(int(sys.stdin.readline().rstrip())):
    point = int(sys.stdin.readline().rstrip())
    if point > num:
        for i in range(point-pushnum):
            pushnum +=1
            li.append(pushnum)
            ll.append('+')
        num = li[len(li)-1]
        if num != point:
            res = False
            break
        li.pop()
        ll.append('-')
    else:
        for i in range(num-point+1):
            li.pop()
            ll.append('-')
    num = li[len(li)-1]

if res:
    for i in ll:
        print(i)
else:
    print("NO")