import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0 for i in range(K+1)]
dp[0] = 1

for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    for j in range(a, K+1):
        dp[j] +=dp[j-a]    

print(dp[K])