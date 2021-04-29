import sys

N = int(sys.stdin.readline().rstrip())

dp = [0 for i in range(1001)]

dp[1] = 1
if 1<N:
    for i in range(2, N+1):
        if i%2 == 0:
            dp[i] = dp[i-1]*2+1
        else:
            dp[i] = dp[i-1]*2-1
print(dp[N]%10007)
