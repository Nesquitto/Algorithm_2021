a = list(map(int, input().split()))
min = a[0]
if min>a[1]:
    min = a[1]
if min>a[2]-a[0]:
    min = a[2]-a[0]
if min>a[3]-a[1]:
    min = a[3]-a[1]
print(min)
