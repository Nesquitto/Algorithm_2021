import sys
N = sys.stdin.readline().rstrip()
isTr = False
for i in range(int(N)-100, int(N)):
    a = i
    b = i
    while(b//10>0):
        a += b%10
        b //= 10
    a += b%10
    if a == int(N):
        isTr = True
        print(i)
        break
if isTr ==False:
    print('0')