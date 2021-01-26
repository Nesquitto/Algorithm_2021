import sys

li = [0 for i in range(10001)]
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    li[int(sys.stdin.readline().rstrip())] +=1
    
for ind, i in enumerate(li):
    for j in range(i):
        print(ind)