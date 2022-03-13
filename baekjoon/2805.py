import sys
N, M = map(int, sys.stdin.readline().split())
inputTree = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(inputTree)
while start <= end:
  mid = (start + end)//2
  sum = 0
  for i in inputTree:
    if i > mid:
      sum += i-mid
  #print(start, mid, end, sum)
  if sum >= M:
    start = mid+1
  else:
    end = mid-1
print(end)