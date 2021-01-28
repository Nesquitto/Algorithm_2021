import sys
N, K = map(int, sys.stdin.readline().split())
W = []
V = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    W.append(a)
    V.append(b)

def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(W+1):  # 각 칸을 돌면서
            if i==0 or w==0:  # 0번째 행/열은 0으로 세팅
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]



print(knapsack(K, W, V, N))