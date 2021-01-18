import sys

dic = {}

N = sys.stdin.readline().rstrip()
a = list(map(int, sys.stdin.readline().split()))
for i in a:
    if(i in dic):
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
M = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    if(i in dic):
        print(dic[i], end=" ")
    else:
        print(0, end=" ")