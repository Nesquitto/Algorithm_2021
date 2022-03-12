import sys

N, M, B= map(int, sys.stdin.readline().split())
inputMap = []
for i in range (N):
  inputMap.append(list(map(int, sys.stdin.readline().split())))

maxHeight = max(map(max, inputMap))
solTime = 10**10
solHeight = 257
for z in range(maxHeight, -1, -1):
  tmpTime = 0
  tmpB = B
  for xArr in inputMap:
    for x in xArr:
      if x > z:
        tmpTime += 2*(x-z)
        tmpB += x-z
      elif x < z:
        tmpTime += (z-x)
        tmpB -= z-x
      else:
        pass
  #print(z, solTime, tmpTime, tmpB)
  if tmpB >= 0:
    if tmpTime < solTime:
      solTime = tmpTime
      solHeight = z
print(solTime, solHeight)
      

 