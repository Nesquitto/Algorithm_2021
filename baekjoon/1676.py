N = int(input())
num = 1
for i in range(1, N+1):
  num *= i
num = reversed(str(num))
solve = 0
for i in num:
  if i == '0':
    solve += 1
  else:
    break
print(solve)
  
