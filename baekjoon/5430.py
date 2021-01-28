import sys
from collections import deque

for T in range(int(sys.stdin.readline().rstrip())):
    error = False
    rev = 0
    command = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    if n > 0:
        num = deque(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))
    else:
        a = sys.stdin.readline()
        num = deque()
    for i in command:
        if(i == 'R'):
            rev +=1
        elif(i == 'D' and len(num) > 0):
            if(rev %2 == 0):
                num.popleft()
            else:
                num.pop()
        else:
            print('error')
            num.clear()
            error = True
            break
    if error:
        continue
    if rev % 2 == 1:
        num.reverse()
    print('[' + ','.join(str(i) for i in list(num)) + ']')
    num.clear()