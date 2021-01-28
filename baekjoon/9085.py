import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    num = []
    num = list(map(int, sys.stdin.readline().split()))
    res = 0
    for k in num:
        res +=k
    print(res)