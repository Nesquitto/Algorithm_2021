import sys
W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
# H//(c+1) 은 다 접은 뒤의 높이, c+1을 곱하면 높이에 해당하는 값을 구할 수 있음(c+1개로 나뉘어졌다는 뜻)
fx1, fx2 = 0, f # 왼쪽 부분
lx1, lx2 = 0, W-f # 오른쪽 부분
kyfx1, kyfx2 = x1, 0
kylx1, kylx2 = x1, 0
if fx2 < x1:
    n = 0
else:
    if fx2 < x2:
        n = fx2-x1
    else:
        n = x2-x1

if lx2 < x1:
    m = 0
else:
    if lx2 < x2:
        m = lx2-x1
    else:
        m = x2-x1

result = (n * (y2-y1) + m * (y2-y1)) *(c+1)
print(kyfx2, kyfx1, y2, y1)
print(n, m)
print(H*W-result)