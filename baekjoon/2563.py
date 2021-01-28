n = int(input())
a = [[0for i in range(100)]for i in range(100)]
for i in range(n):
    xy = list(map(int, input().split()))
    for j in range(10):
        for k in range(10):
            a[xy[0]+j-1][xy[1]+k-1] = 1
total = 0
for i in range(100):
    for j in range(100):
        if a[i][j] == 1:
            total = total +1
print(total)