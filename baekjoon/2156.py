import sys

N = int(sys.stdin.readline().rstrip())
dp = [0 for i in range(N)]
wine = []
for i in range(N):
    wine.append(int(sys.stdin.readline().rstrip()))

if N == 1:
    res = wine[0]
elif N == 2:
    res = wine[0]+wine[1]
else:
    dp[0] = wine[0]
    dp[1] = dp[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], wine[0]+wine[1])
    for i in range(3, N):
        dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i], dp[i-1])
    res = dp[N-1]
print(res)
