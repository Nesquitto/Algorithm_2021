N = int(input())
i = 1
num = 1
while True:
  if N == 1:
    print(1)
    break
  num += 6*i
  i += 1
  if num>=N:
    print(i)
    break