def jae(num, a, m, n, k = 0):
    start = (m-n)//2
    if(k == m**2 or n == 0):
        return 0
    if(n == 1):
        a[start][start] = m**2-k

    for i in range(n):
        a[start+i][start] = m**2-k
        if(m**2-k == num):
            a[m][0] = start + i +1
            a[m][1] = start +1
        k = k+1

    for i in range(start+1, start+n):
        a[m-start-1][i] = m**2-k
        if(m**2-k == num):
            a[m][0] = m-start-1 +1
            a[m][1] = i +1
        k = k+1
    for i in range(start+1, start+n):
        a[m-i-1][m-start-1] = m**2-k
        if(m**2-k == num):
            a[m][0] = m-i-1 +1
            a[m][1] = m-start-1 +1
        k = k+1
    for i in range(start+1, start+n-1):
        a[start][m-i-1] = m**2-k
        if(m**2-k == num):
            a[m][0] = start +1
            a[m][1] = m-i-1 +1
        k = k+1

    jae(num, a, m, n-2, k)



a = int(input())
b = int(input())
ret = [[0 for i in range(a)] for j in range(a+1)]
jae(b, ret, a, a)
for i in range(a+1):
    for j in range(a):
        if(i == a and j >= 2):
            continue
        print("{} ".format(ret[i][j]), end='')
    print()
