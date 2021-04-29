import sys

N = int(sys.stdin.readline().rstrip())
info = []
res = []
count = 0
for i in range(N):
    info.append(list(sys.stdin.readline()))

def dfs(info, x, y):
    global count
    count += 1
    info[x][y] =0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        if x + dx[i] >=0 and x + dx[i] <N and y + dy[i] >=0 and y +dy[i] <N and info[x+dx[i]][y+dy[i]] == '1':
            dfs(info, x + dx[i], y + dy[i])

for i in range(N):
    for j in range(N):
        if info[i][j] == '1':
            count = 0
            dfs(info, i, j)
            res.append(count)
            
print(len(res))
res.sort()
for i in res:
    print(i)