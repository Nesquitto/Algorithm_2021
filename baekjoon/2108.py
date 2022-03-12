from collections import Counter
N = int(input())
numList = []
for _ in range(N):
  numList.append(int(input()))
print(round(sum(numList)/N))
sortedList = sorted(numList)
print(sortedList[N//2])
cnt = Counter(sortedList)
tmpCommon = cnt.most_common()
if N != 1:
  if tmpCommon[0][1] == tmpCommon[1][1]:
    print (tmpCommon[1][0])
  else:
    print (tmpCommon[0][0])
else:
  print(tmpCommon[0][0])
print(-1 * (sortedList[0]-sortedList[N-1]))