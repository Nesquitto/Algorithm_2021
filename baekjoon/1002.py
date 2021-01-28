import sys
import math
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    res = (x2-x1)**2+(y2-y1)**2
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print('-1')
        else:
            print('0')
    else:
        if (r1+r2)**2 < res:
            print('0')
        elif (r1+r2)**2 == res:
            print('1')
        else:
            if (r1-r2)**2 == res:
                print('1')
            elif (r1-r2)**2 > res:
                print('0')
            else:
                print('2')