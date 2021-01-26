import sys

a = int(sys.stdin.readline().rstrip())
se = set(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().split()))
for i in li:
    if i in se:
        print('1', end=" ")
    else:
        print('0', end=" ")    