a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(b)):
    b[i] = b[i]-a[0]*a[1]
    print("{} ".format(b[i]), end='')
