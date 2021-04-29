import sys

N, K = map(int, sys.stdin.readline().split())

sec = abs(K-N)

def solve(depth, N):
    global K
    global sec
    if depth  == sec:
        return
    if N == K:
        sec = depth
        return
    solve(depth+1, N*2)
    solve(depth+1, N+1)
    solve(depth+1, N-1)


solve(0, N)
print(sec)