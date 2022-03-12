L = input()
inputString = input()
M = 1234567891
r = 31
H = 0
for i in range(len(inputString)):
  H += (ord(inputString[i])-96)*(r**i)
H %= M
print (H)