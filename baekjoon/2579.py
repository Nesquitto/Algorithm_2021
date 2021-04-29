import sys

N = int(sys.stdin.readline().rstrip())
score = 0
stair = list(0 for i in range(N+1))
dp = list(0 for i in range(N +1))
for i in range(1, N+1):
    stair[i] = (int(sys.stdin.readline().rstrip()))
if N ==1 :
    dp[1] = stair[1]
elif N ==2:
    dp[2] = stair[1] + stair[2]
else:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(dp[1] + stair[3], stair[2]+ stair[3])
    for i in range(4, N+1):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])



print(dp[N])