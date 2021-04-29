import sys

N = int(sys.stdin.readline().rstrip())

tri = []
for i in range(N):
    tri.append(list(map(int, sys.stdin.readline().split()))) #역삼각형
tri.reverse()
for i in range(len(tri)):
    for j in range(len(tri[i])-1):
        tri[i+1][j] += max(tri[i][j], tri[i][j+1])
print(tri[N-1][0])