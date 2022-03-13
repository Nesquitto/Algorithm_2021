import sys
T = int(sys.stdin.readline().rstrip())

for _ in range (T):
  N, M = map(int, sys.stdin.readline().split())
  inputDoc = list(map(int, sys.stdin.readline().split()))
  tmpDoc = inputDoc[:]
  tmpMax = max(tmpDoc)
  sol = 0
  isSol = False
  for i in range(9, 0, -1):
    for num, j in enumerate(inputDoc):
      if tmpMax == j:
        sol += 1
        if M == num:
          print(sol)
          isSol = True
          break
        tmpDoc.remove(tmpMax)
        tmpMax = max(tmpDoc)
    if isSol:
      break

  