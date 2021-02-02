import sys

N = int(sys.stdin.readline().rstrip())
res = []

def solve(numlist, num):
    global N
    global res
    numlist.append(num)
    if len(res) !=0:
        return
    for i in range(len(numlist)//2):
        if numlist[(-1-i)*2:-1-i] == numlist[-1-i:]:
            return
    if len(numlist) == N:
        res = numlist
        return
    solve(numlist[:], '1')
    solve(numlist[:], '2')
    solve(numlist[:], '3')
        

solve([], '1')
print("".join(i for i in res))