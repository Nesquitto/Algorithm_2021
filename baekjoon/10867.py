import sys

a = input()
number = set(map(int, sys.stdin.readline().split()))
print(" ".join(str(i) for i in sorted(number)))