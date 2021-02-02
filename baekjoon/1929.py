import sys
from math import sqrt

M, N = map(int, sys.stdin.readline().split())

erathos = [True]*(N+1)
for i in range(2, int(sqrt(N))+1):
    if erathos[i]:
        for j in range(i+i, N+1, i):
            erathos[j] = False

for ind, i in enumerate(erathos):
    if i and ind>=M and ind <= N and ind != 1:
        print(ind)