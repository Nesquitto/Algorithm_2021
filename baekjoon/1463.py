a = int(input())
def jae(b, c, d):
    if d > 29:
        return
    if b <= 1:
        liss.append(d-1)
        return
    if c == 1:
        b = b//3
        if b % 3 == 0:
            jae(b, 1, d+1)
        if b % 2 == 0:
            jae(b, 2, d+1)
        if b % 3 != 0 or b % 2 != 0:
            jae(b, 3, d+1)
    elif c == 2:
        b = b//2
        if b % 3 == 0:
            jae(b, 1, d+1)
        if b % 2 == 0:
            jae(b, 2, d+1)
        if b % 3 != 0 or b % 2 != 0:
            jae(b, 3, d+1)
    else:
        b = b-1
        if b % 3 == 0:
            jae(b, 1, d+1)
        if b % 2 == 0:
            jae(b, 2, d+1)
        if b % 3 != 0 or b % 2 != 0:
            jae(b, 3, d+1)

liss = []
d = 0
if a % 3 == 0:
    jae(a, 1, d+1)
if a % 2 == 0:
    jae(a, 2, d+1)
if a % 3 != 0 or a % 2 != 0:
    jae(a, 3, d+1)
print(a, min(liss))