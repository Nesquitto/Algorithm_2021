def jae(a, m, n, k = 1):
    start = (m-n)//2
    if(k > m**2 or n == 0):
        return 0
    if(n == 1):
        a[start][start] = k

    for i in range(n):
        a[start][start+i] = k
        k = k+1
    for i in range(start+1, start+n):
        a[i][m-start-1] = k
        k = k+1
    for i in range(start+1, start+n):
        a[m-start-1][m-i-1] = k
        k = k+1
    for i in range(start+1, start+n-1):
        a[m-i-1][start] = k
        k = k+1
    jae(a, m, n-2, k)



a = int(input())
ret = [[0 for i in range(a)] for j in range(a)]
jae(ret, a, a)
for i in range(a):
    for j in range(a):
        print("{}\t".format(ret[i][j]), end='')
    print()
