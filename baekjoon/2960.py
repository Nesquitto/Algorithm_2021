import sys
import math
N, K = map(int, sys.stdin.readline().split())
arr = [True] * (N+1)
num = 0
for i in range(2, N+1):
    if arr[i] == True:
        for j in range(i, N+1, i):
            if arr[j] == True:
                num = num+1
                if num == K:
                    print(j)
            arr[j] = False

