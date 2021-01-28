import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
res = deque(i for i in range(1, N+1))
sol = list()

while(len(res) >0):
    res.rotate(-(K-1))
    sol.append(res.popleft())

print("<" + ", ".join(str(i) for i in sol), end=">")
