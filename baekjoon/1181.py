a = int(input())
b = []
c = []
for i in range(a):
    b.append(input())
b = set(b)
b = list(b)
b = sorted(b)
for i in range(len(b)):
    c.append(len(b[i]))
for i in range(1, max(c)+1):
    for j in range(len(b)):
        if c[j] == i:
            print(b[j])


