from collections import deque
inputStr = deque(input())
boomStr = list(input())
boomLastChar = boomStr[-1]
boomLen = len(boomStr)
tmpList = []
tmpLen = 0

#FLURA
for i in range(len(inputStr)):
  tmpString = inputStr.popleft()
  tmpList.append(tmpString)
  tmpLen += 1
  if tmpString == boomLastChar and tmpLen >= boomLen:
    if tmpList[-boomLen:] == boomStr:
      for j in range(boomLen):
        tmpList.pop()
      tmpLen -= boomLen
if len(tmpList) != 0:
  print(''.join(tmpList))
else:
  print("FRULA")