import sys
for i in range(int(sys.stdin.readline())):
    op = 0
    cl = 0
    rig = True
    a = sys.stdin.readline()
    for j in a:
        if j == '(':
            op += 1
        elif j == ')':
            cl += 1
        if op < cl:
            rig = False
            break
    if rig and op == cl:
        print('YES')
    else:
        print('NO')


