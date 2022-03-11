import sys
N = int(sys.stdin.readline().rstrip())
isAns = False
for i in range(N):
  sum = i
  for j in str(i):
    sum += int(j)
  if sum == N:
    isAns = True
    print(i)
    break
if isAns == False:
    print('0')