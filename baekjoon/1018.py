c = list(map(int, input().split()))
d = []
count = []
for i in range(c[0]):
    d.append(input())
for n in range(0, c[0]-7):
    for m in range(0, c[1]-7):
        a, b = 0, 0
        for i in range(n, n+8):
            for j in range(m, m+8):
                if (i%2 ==0 and j%2 == 0) or (i%2 == 1 and j % 2 == 1):
                    if d[i][j] == "W":
                        a = a + 1
                if (i%2 ==1 and j%2 == 0) or (i%2 == 0 and j % 2 == 1):
                    if d[i][j] == "B":
                        a = a + 1
                if (i%2 ==0 and j%2 == 0) or (i%2 == 1 and j % 2 == 1):
                    if d[i][j] == "B":
                        b = b + 1
                if (i%2 ==1 and j%2 == 0) or (i%2 == 0 and j % 2 == 1):
                    if d[i][j] == "W":
                        b = b + 1
        count.append(a)
        count.append(b)
print(min(count))
