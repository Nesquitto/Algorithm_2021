a = [0 for i in range(3)]
x = 1
for i in range(3):
    a[i] = int(input())
    x = x * a[i]
x = str(x)
b = [0 for i in range(10)]
for i in range(len(x)):
    b[int(x[i])] = b[int(x[i])] + 1

for i in range(len(b)):
    print(b[i])