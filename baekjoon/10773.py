import sys
from collections import deque
K = int(sys.stdin.readline().rstrip())
solDeque = deque()
for _ in range(K):
  tmpNum = int(sys.stdin.readline().rstrip())
  if tmpNum != 0:
    solDeque.append(tmpNum)
  else:
    solDeque.pop()
print(sum(solDeque))