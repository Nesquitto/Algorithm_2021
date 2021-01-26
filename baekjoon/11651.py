import sys

point = []
for i in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().split())
    point.append([x,y])
point.sort(key= lambda x: (x[1], x[0]))
for i in point:
    print(i[0], i[1])