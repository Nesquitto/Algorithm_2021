import math

solveMin = 4
def SolveFunc(time, num, sub):
  global solveMin
  #print(solveMin, time, num, sub)
  num -= sub**2
  if num == 0:
    solveMin = time
    return
  if time+1 >= solveMin:
    return
  if math.floor(math.sqrt(num))>sub:
    return
  for i in range(math.floor(math.sqrt(num)), 0, -1):
    SolveFunc(time + 1, num, i)
    
n = int(input())

for i in range(math.floor(math.sqrt(n)), 0, -1):
  SolveFunc(1, n, i)
print(solveMin)