import sys

N = int(sys.stdin.readline().rstrip())

l = []

for i in range(N):
    a, b = sys.stdin.readline().split()
    l.append([int(a), b])
l.sort(key=lambda x:x[0])

for i in l:
    print(i[0], i[1])