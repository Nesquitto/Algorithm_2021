import sys
a, b = map(int, sys.stdin.readline().split())
name = {}
d = {}
pro = []
for i in range(1, a+1):
    c = sys.stdin.readline().rstrip()
    name[i] = c
    d[c] = i
for i in range(b):
    pro = sys.stdin.readline().rstrip()
    if pro.isdigit():
        print(name[int(pro)])
    else:
        print(d[pro])