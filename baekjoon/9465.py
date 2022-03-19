import sys
T = int(sys.stdin.readline().rstrip())
T = 1 ####
for i in range(T):
  inputList = []
  n = int(sys.stdin.readline().rstrip())
  n = 5 ####
  for i in range(2):
    inputList.append(list(map(int, sys.stdin.readline().split())))
  inputList[0] = [50, 10, 100, 20, 40] ####
  inputList[1] = [30, 50, 70, 10, 60] ####
  solveList[0 for i in range(n)]
  for i in range(n):
    if i == 0:
      solveList[0] = max(inputList[0][0], inputList[1][0])
    elif i == 1:
      