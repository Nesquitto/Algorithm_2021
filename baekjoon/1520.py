import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
data = []
dp = [[0for i in range(N)]for i in range(M)]
a = [1, -1, 0, 0]
b = [0, 0, 1, -1]
queue = deque()
queue.append([0,0])
dp[0][0] = 1

for i in range(M):
    data.append(list(map(int, sys.stdin.readline().split())))

while queue:
    n = queue.popleft()
    for i in range(4):
        x = n[0] + a[i]
        y = n[1] + b[i]
        if 0 <= x < M and 0 <= y < N:
            if data[x][y] < data[n[0]][n[1]]:
                queue.append([x,y])
                dp[x][y] += dp[n[0]][n[1]]

print(dp)

print(dp[M-1][N-1])
