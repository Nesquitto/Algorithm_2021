#print("2775.py")
solList = [[0 for i in range(15)] for _ in range(15)]
solList[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i in range(1,15):
  for j in range(1,15):
    solList[i][j] = solList[i-1][j]+solList[i][j-1]
T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())
  print(solList[k][n])