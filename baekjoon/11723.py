import sys
M = int(sys.stdin.readline().rstrip())
solSet = set()
for _ in range(M):
  inputCommand = list(sys.stdin.readline().split())
  if inputCommand[0] == "add":
    solSet.add(int(inputCommand[1]))
  elif inputCommand[0] == "remove":
    solSet.discard(int(inputCommand[1]))
  elif inputCommand[0] == "check":
    if int(inputCommand[1]) in solSet:
      print(1)
    else:
      print(0)
  elif inputCommand[0] == "toggle":
    if int(inputCommand[1]) in solSet:
      solSet.discard(int(inputCommand[1]))
    else:
      solSet.add(int(inputCommand[1]))
  elif inputCommand[0] == "all":
    solSet = {_ for _ in range(1,21)}
  elif inputCommand[0] == "empty":
    solSet = set()