import sys
K, N = map(int, sys.stdin.readline().split())
lanCable = list()
for i in range(K):
  lanCable.append(int(sys.stdin.readline().rstrip()))
minLen = 1
maxLen = max(lanCable)
midLen = 0
solve = 0
while maxLen >= minLen:
  solve = 0
  midLen = (minLen + maxLen)//2
  for i in lanCable:
    solve += i//midLen
  if solve < N:
    maxLen = midLen -1
  else:
    minLen = midLen +1
print(maxLen)