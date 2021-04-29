import sys
from collections import deque

N, M, H= map(int, sys.stdin.readline().split())
data = []
can = True
day = 0
a = [1, -1, 0, 0, 0, 0]
b = [0, 0, 1, -1, 0, 0]
c = [0, 0, 0, 0, 1, -1]
stack = deque()
for i in range(H):
    temp = []
    for i in range(M):
        temp.append(list(map(int, sys.stdin.readline().split())))
    data.append(temp)
for x, i in enumerate(data):
    for y, j in enumerate(i):
        for z, k in enumerate(j):
            if k == 1:
                stack.append([x, y, z])
while stack:
    n = stack.popleft()
    for i in range(6):
        z = n[0]+a[i]
        x = n[1]+b[i]
        y = n[2]+c[i]
        if 0 <= x < M and 0 <= y < N and 0 <= z < H:
            if data[z][x][y] == 0:
                stack.append([z, x, y])
                data[z][x][y] = data[n[0]][n[1]][n[2]] + 1
for i in data:
    for j in i:
        for k in j:
            if day  < k:
                day = k
            if k == 0:
                can = False
if can == False:
    print(-1)
elif day == 1:
    print(0)
else:
    print(day-1)