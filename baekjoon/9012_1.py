import sys

for i in range(int(sys.stdin.readline().rstrip())):
    res = 'YES'
    li = list(sys.stdin.readline().rstrip())
    ll = []
    for j in li:
        if j == '(':
            ll.append(True)
        elif j == ')' and len(ll) >0:
            ll.pop()
        else:
            res = 'NO'
    if len(ll) !=0:
        res = 'NO'
    print(res)