import sys
import math
count = 0
def era(m):
    im = [True] * m
    for i in range(2, int(math.sqrt(m))):
        if im[i]:
            for j in range(i+i, m, i):
                im[j] = False
    return [i for i in range(2,m) if im[i]]
a = sys.stdin.readline().rstrip()
ls = list(map(int, sys.stdin.readline().split()))
erathos = era(1000)
for i in range(int(a)):
    if ls[i] in erathos:
        count = count+1
print(count)

