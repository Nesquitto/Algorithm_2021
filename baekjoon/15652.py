from itertools import combinations_with_replacement

N, M = map(int,input().split())

solveList = list(combinations_with_replacement([i for i in range(1, N+1)], M))

for i in solveList:
  for j in i:
    print(j, end=" ")
  print()