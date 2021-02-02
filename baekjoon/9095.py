import sys
from itertools import combinations

T = int(sys.stdin.readline().rstrip())
case = list()
res = 0

def combi(n, case):
    if n>=3:
        case.append(3)
        combi(n-3, case)
    if n>=2:
        case.append(2)
        combi(n-2, case)
    if n>=1:
        case.append(1)
        combi(n-1, case)
    if n == 0:
        global res
        res += len(list(combinations(case, len(case))))


for i in range(T):
    res = 0
    combi(int(sys.stdin.readline().rstrip()), case)
    print(res)