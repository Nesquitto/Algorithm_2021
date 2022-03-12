N = int(input())
inputList = []
for _ in range(N):
  x, y = map(int, input().split())
  inputList.append([x, y, -1])
for num, i in enumerate(inputList):
  order = 1
  for j in inputList:
    if i[0]<j[0] and i[1]<j[1]:
      order +=1
  inputList[num][2] = order
for i in inputList:
  print(i[2], end=" ")