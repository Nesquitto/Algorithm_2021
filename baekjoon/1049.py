import sys
ls = []
a, b = map(int, sys.stdin.readline().split())
for i in range(b):
    ls.append(tuple(map(int, sys.stdin.readline().split())))
minmo = 1000
minpa = 1000
for i in range(b):
    if minmo > ls[i][1]:
        minmo = ls[i][1]
    if minpa > ls[i][0]:
        minpa = ls[i][0]

if minpa>minmo*6:
    print(minmo*a)
else:
    if (a%6)*minmo >minpa:
        print((a//6+1)*(minpa))
    else:
        print((a//6)*minpa + (a%6)*minmo)