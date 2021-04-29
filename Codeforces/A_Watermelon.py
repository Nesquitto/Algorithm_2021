import sys

a = int(sys.stdin.readline().rstrip())
b = False
for i in range(2, a+1, 2):
    if i %2 == 0 and (a-i) %2 == 0 and a-i>0:
        b = True
if b:
    print("YES")
else:
    print("NO")