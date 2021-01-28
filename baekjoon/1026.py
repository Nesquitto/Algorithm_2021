import sys
a = int(sys.stdin.readline().rstrip())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
B = sorted(list(map(int, sys.stdin.readline().split())))
res = 0
for i in range(a):
    res = res + A[i] * B[i]
print(res)