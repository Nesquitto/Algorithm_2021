import sys
here = set([])
see = set([])
a, b = map(int, sys.stdin.readline().split())
for i in range(a):
    here.add(sys.stdin.readline().rstrip())
for i in range(b):
    see.add(sys.stdin.readline().rstrip())
res = here & see
res = sorted(list(res))
print(len(res))
for i in range(len(res)):
    print(res[i])