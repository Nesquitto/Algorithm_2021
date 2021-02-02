import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
people = [i for i in range(N)]
info = []
min = 100000
devsum = 0
devsum2 = 0

for i in range(N):
    info.append(list(map(int, sys.stdin.readline().split())))    

for i in range(N):
    for j in range(i+1, N):
        info[i][j] +=info[j][i]

dev = list(combinations(people, N//2))
for i in dev:
    for j in range(N):
        for k in range(j+1, N):
            if j in i and k in i:
                devsum += info[j][k]
            if j not in i and k not in i:
                devsum2 +=info[j][k]
    if min > abs(devsum - devsum2):
        min = abs(devsum-devsum2)
    devsum = 0
    devsum2 = 0

    

print(min)

