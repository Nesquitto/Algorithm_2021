import sys
time = list()
end = 0
val = 0
for i in range(int(sys.stdin.readline().rstrip())):
    time.append(list(map(int, sys.stdin.readline().split())))
time = sorted(time, key=lambda a:a[0])
time = sorted(time, key=lambda a:a[1])
print(time)
for i in time:
    if(i[0] >= end):
        val += 1
        end = i[1]
print(val)