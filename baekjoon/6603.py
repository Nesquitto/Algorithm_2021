import sys

from itertools import combinations

while(True):
    inf = list(map(int, sys.stdin.readline().split()))
    if(inf[0] == 0):
        break
    else:
        del inf[0]
        a = list(combinations(inf, 6))
        for i in a:
            print(" ".join(str(j) for j in i))
    print()