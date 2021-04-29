import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = []
a = [1, -1, 0, 0]
b = [0, 0, 1, -1]
stack = deque()
stack.append([0,0])
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().rstrip())))

while stack:
    n = stack.popleft()
    for i in range(4):
        x = n[0]+a[i]
        y = n[1]+b[i]
        if 0 <= x < N and 0 <= y < M:
            if data[x][y] == 1:
                stack.append([x,y])
                data[x][y] = data[n[0]][n[1]] + 1
print(data[N-1][M-1])