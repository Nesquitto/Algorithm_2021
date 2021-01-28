a = int(input())
a0, a1 = 0, 1
while(a-1):
    a0, a1 = a1, a0+a1
    a = a-1
print(a1)