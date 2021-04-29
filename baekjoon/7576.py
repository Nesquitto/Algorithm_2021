import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = []
can = True
day = 0
a = [1, -1, 0, 0]
b = [0, 0, 1, -1]
stack = deque()
for i in range(M):
    data.append(list(map(int, sys.stdin.readline().split())))
for x, i in enumerate(data):
    for y, j in enumerate(i):
        if j == 1:
            stack.append([x, y])
while stack:
    n = stack.popleft()
    for i in range(4):
        x = n[0]+a[i]
        y = n[1]+b[i]
        if 0 <= x < M and 0 <= y < N:
            if data[x][y] == 0:
                stack.append([x,y])
                data[x][y] = data[n[0]][n[1]] + 1
for i in data:
    for j in i:
        if day  < j:
            day = j
        if j == 0:
            can = False
if can == False:
    print(-1)
elif day == 1:
    print(0)
else:
    print(day-1)