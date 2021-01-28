import sys

fiboarr = [[0 for i in range(2)]for i in range(41)]
arr = 1
fiboarr[0][0], fiboarr[0][1] = 1, 0
fiboarr[1][0], fiboarr[1][1] = 0, 1
def fibo(n):
    global arr
    if(arr>n):
        return
    for i in range(arr+1, n+1):
        fiboarr[i][0], fiboarr[i][1] = fiboarr[i-2][0]+fiboarr[i-1][0], fiboarr[i-2][1]+fiboarr[i-1][1]
    arr = n
    return

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    fibo(N)
    print(fiboarr[N][0], fiboarr[N][1])