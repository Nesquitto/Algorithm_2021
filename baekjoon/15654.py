from itertools import permutations

N, M = map(int,input().split())

solveList = list(permutations(sorted(list(map(int, input().split()))), M))

for i in solveList:
  for j in i:
    print(j, end=" ")
  print()