import sys

N = int(sys.stdin.readline().rstrip())

dp = list(map(int, sys.stdin.readline().split()))
sol = [0 for i in range(N)]
sol[0] = dp[0]
for i in range(1, N):
    sol[i] = max(dp[i], sol[i-1]+dp[i])
print(max(sol))