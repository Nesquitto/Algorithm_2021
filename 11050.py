import sys

N, K = map(int, sys.stdin.readline().split())

if (K < 0) or K>N:
    answer = 0
else:
    tmp = 1
    tmp2 = 1
    tmp3 = 1
    for i in range(1, N+1):
        tmp = tmp*i
    for i in range(1, K+1):
        tmp2 = tmp2*i
    for i in range(1, N-K+1):
        tmp3 = tmp3*i
    answer = tmp/(tmp2*tmp3)
print(int(answer))