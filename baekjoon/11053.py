N = int(input())
inputList = list(map(int, input().split()))

lenList = [0 for i in range(N)]
for i in range(N):
  if i == 0:
    lenList[i] = 1
    continue
  num = 0
  for j in range(i):
    if inputList[i] > inputList[j]:
      if num < lenList[j]:
        num = lenList[j]
  lenList[i] = num + 1
print(max(lenList))