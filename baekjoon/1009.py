import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  if a%10 == 0:
    print(10)
  elif a%10 == 1:
    print(1)
  elif a%10 == 2:
    li = [6, 2, 4, 8]
    print(li[b%4])
  elif a%10 == 3:
    li = [1, 3, 9, 7]
    print(li[b%4])
  elif a%10 == 4:
    li = [6, 4]
    print(li[b%2])
  elif a%10 == 5:
    print(5)
  elif a%10 == 6:
    print(6)
  elif a%10 == 7:
    li = [1, 7, 9, 3]
    print (li[b%4])
  elif a%10 == 8:
    li = [6, 8, 4, 2]
    print (li[b%4])
  elif a%10 == 9:
    li = [1, 9]
    print (li[b%2])