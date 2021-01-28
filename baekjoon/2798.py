import sys
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
min = 100000
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if min > M-(a[i]+a[j]+a[k]) and M-(a[i]+a[j]+a[k]) >= 0:
                min = M-(a[i]+a[j]+a[k])
                res = a[i]+a[j]+a[k]
print(res)

