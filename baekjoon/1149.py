import sys

N = int(sys.stdin.readline().rstrip())\

dp = list()
for i in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(N-1):
    dp[i+1][0] += min(dp[i][1], dp[i][2])
    dp[i+1][1] += min(dp[i][0], dp[i][2])
    dp[i+1][2] += min(dp[i][1], dp[i][0])  
    
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))