import sys

N = int(sys.stdin.readline().rstrip())
li = set(sys.stdin.readline().split())
M = int(sys.stdin.readline().rstrip())
lil = list(sys.stdin.readline().split())
for i in lil:
    if i in li:
        print(1)
    else:
        print(0)