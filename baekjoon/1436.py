import sys

N = int(sys.stdin.readline().rstrip())
i = 0
num = 665
while i != N:
    num += 1
    if '666' in str(num):
        i = i + 1
print(num)