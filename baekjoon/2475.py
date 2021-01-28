a = input().split()
a = list(a)
for i in range(len(a)):
    a[i] = int(a[i])**2

print(sum(a)%10)