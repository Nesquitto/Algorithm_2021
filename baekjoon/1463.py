import sys
min = 100000
N = int(sys.stdin.readline().rstrip())

def sol(N, calc):
    global min
    if calc == min or N < 1:
        return
    if N == 1:
        min = calc
        return
    if N % 3 == 0:
        sol(N/3, calc+1)
    if N % 2 == 0:
        sol(N/2, calc+1)
    sol(N-1, calc+1)


sol(N, 0)
print(min)