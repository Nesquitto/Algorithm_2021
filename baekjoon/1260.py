import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
line = []
point = []
for i in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))
dfsorder = []
bfsorder = []
br = 0

def dfs(point, start):
    global line
    global dfsorder
    cango = list()
    stack = deque([start]) # 처음 시작점을 큐에 집어넣음
    while stack: # 스택이 다 빌 때까지
        n = stack.pop() # 맨 뒤의 정점을 뺌
        if n not in point: # 해당 정점이 처음 도달한 정점일 때
            cango.clear()
            point.append(n)
            dfsorder.append(n)
            for i in line:
                if n in i:
                    if n == i[0]:
                        cango.append(i[1])
                    else:
                        cango.append(i[0])
            cango.sort()
            cango.reverse()
            stack.extend(cango)

def bfs(point, start):
    global line
    global bfsorder
    cango = list()
    queue = deque([start]) # 처음 시작점을 큐에 집어넣음
    while queue: # 큐가 다 빌 때까지
        n = queue.popleft() # 맨 앞의 정점을 뺌
        if n not in point: # 해당 정점이 처음 도달한 정점일 때
            cango.clear()
            point.append(n)
            bfsorder.append(n)
            for i in line:
                if n in i:
                    if n == i[0]:
                        cango.append(i[1])
                    else:
                        cango.append(i[0])
            cango.sort()
            queue.extend(cango)



dfs(point[:], V)

bfs(point[:], V)

print(" ".join(str(i) for i in dfsorder))
print(" ".join(str(i) for i in bfsorder))