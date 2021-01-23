import sys

N, K = map(int, sys.stdin.readline().split())
li = [i for i in range(1, N+1)]
ll = []
a = K-1
for i in range(N):
    ll.append(li[a])
    del li[a]
    if(N-i-1 > 0):
        a = ((a + K-1)%(N-i-1))
print("<", end='')
for i in range(len(ll)):
    if(i !=len(ll)-1):
        print(ll[i], end=', ')
    else:
        print(ll[i], end=">")

