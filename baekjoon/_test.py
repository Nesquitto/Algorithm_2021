
numlist = "ABCDEFGHIJKLMNOP"

for i in range(len(numlist)//2):
     print(numlist[(-1-i)*2:-1-i])
     print(numlist[-1-i:])