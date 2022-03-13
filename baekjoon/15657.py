from itertools import combinations_with_replacement 

N, M = map(int,input().split())

solveList = list(combinations_with_replacement(sorted(list(map(int, input().split()))), M))

for i in solveList:
  for j in i:
    print(j, end=" ")
  print()