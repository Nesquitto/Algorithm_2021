import sys
n = int(sys.stdin.readline().rstrip())
a = list()
for i in range(n):
    a .append(list(map(int, sys.stdin.readline().split())))

a.sort()

for i in a:
    print (str(i[0]), str(i[1]))
