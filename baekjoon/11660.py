import sys
N, M = map(int, sys.stdin.readline().split())
inputMap = []
for i in range(N):
  inputMap.append(list(map(int, sys.stdin.readline().split())))
sumMap = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N+1):
  for j in range(N+1):
    if i == 0 or j == 0:
      continue
    sumMap[i][j] = sumMap[i][j-1] + sumMap[i-1][j] - sumMap[i-1][j-1] + inputMap[i-1][j-1]
for i in range(M):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  print(sumMap[x2][y2]-sumMap[x2][y1-1]-sumMap[x1-1][y2]+sumMap[x1-1][y1-1])