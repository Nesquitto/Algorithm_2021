t = int(input())
a = []
def facto(a):
    ret = 1
    for i in range(1, a+1):
        ret = ret * i
    return ret

for i in range(t):
    a.append(tuple(map(int, input().split())))
for i in range(t):
    print(facto(a[i][1])//facto(a[i][0])//facto(a[i][1]-a[i][0]))