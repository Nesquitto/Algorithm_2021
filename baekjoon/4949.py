from collections import deque
import sys

while True:
  inputString = sys.stdin.readline().rstrip()
  if inputString == ".":
    break
  checkDeque = deque()
  isOk = True
  for i in inputString:
    if i == "(" or i == "[":
      checkDeque.append(i)
    elif i == ")" or i == "]":
      if len(checkDeque) == 0:
        isOk = False
        break
      tmpChar = checkDeque.pop()
      if i == ")" and tmpChar != "(":
        isOk = False
        break
      elif i == "]" and tmpChar != "[":
        isOk = False
        break
  if len(checkDeque) != 0:
    isOk = False
  if isOk:
    print("yes")
  else:
    print("no")



      