a = int(input())
b = []
for i in range(a):
    b.append(tuple(input().split()))
for i in range(a):
    for j in range(len(b[i][1])):
        print(b[i][1][j]*int(b[i][0]), end="")
    print()
