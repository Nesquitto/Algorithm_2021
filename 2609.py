import sys

a, b = map(int, sys.stdin.readline().split())

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
def LCM(a, b):
    g = GCD(a, b)
    return g * (a/g) * (b/g)

print(GCD(a, b))
print(int(LCM(a, b)))