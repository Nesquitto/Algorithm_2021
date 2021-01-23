import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    H2 = int(N%H)
    W2 = int(N/H+1)
    if H2 == 0:
        print(H*100+(W2-1))
    else:
        print(H2*100+W2)