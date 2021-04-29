import sys

wei = list()
val = 0
sum = 0
max = 0
for i in range(int(sys.stdin.readline().rstrip())):
    wei.append(int(sys.stdin.readline().rstrip()))
wei.sort(reverse=True)
for i in wei:
    val += 1
    if val * i > max:
        max = val * i
print(max)