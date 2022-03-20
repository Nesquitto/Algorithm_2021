A, inputB, C = map(int, input().split())

def Solve(B):
  global A, C
  if B == 1:
    return (A%C)
  elif B == 0:
    return (1%C)
  if B % 2 == 1:
    return (Solve(B//2)**2)*A%C
  else:
    return (Solve(B//2)**2)%C
print(Solve(inputB))