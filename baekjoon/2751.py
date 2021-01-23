import sys
list = []
for i in range(int(sys.stdin.readline())):
    list.append(int(sys.stdin.readline()))
list.sort()
for i in list:
    print(i)