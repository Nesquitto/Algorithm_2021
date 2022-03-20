T = int(input())
for i in range(T):
  x, y = map(int, input().split())
  distance = y-x
  if distance <=2:
    count = distance
  else:
    count = 3 # 횟수
    addNum = 2 # 같은 횟수인 개수
    checkNum = 0 # 0 1을 왓다갔다
    tmpDis = 4 # 가상의 거리
    while tmpDis < distance:
      #print(count, addNum, tmpDis, checkNum)
      if checkNum == 0:
        tmpDis += addNum
        checkNum = 1
        count += 1
      else:
        checkNum = 0
        addNum +=1
        tmpDis += addNum
        count += 1
  print(count)