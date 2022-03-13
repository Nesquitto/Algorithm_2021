from itertools import combinations

N, M = map(int,input().split())

solveList = list(combinations([i for i in range(1, N+1)], M))

for i in solveList:
  for j in i:
    print(j, end=" ")
  print()