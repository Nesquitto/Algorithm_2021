a = int(input())

def erathos():
    sieve = [True] *1000000
    for i in range(2, 1001):
        if sieve[i] == True:
            for j in range(i+i, 1000000, i):
                sieve[j] = False
    return [i for i in range(2, 1000000) if sieve[i] == True]

era = erathos()
ans = True
for i in range(a):
    b = int(input())
    for j in range(len(era)):
        if b % era[j] == 0:
            ans = False
            break
    if ans == True:
        print("YES")
    else:
        print("NO")
    ans = True
