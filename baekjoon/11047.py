import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))

sol = 0
coin.reverse()
for i in coin:
    if K//i > 0:
        sol += K // i
        K %= i
    if K == 0:
        break
print(sol)