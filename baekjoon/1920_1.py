N = input()
A = list(map(int, input().split()))
M = input()
B = list(map(int, input().split()))
A = sorted(A)
for i in range(int(M)):
    left = 0
    right = int(N)-1
    R = False
    while left <= right:
        mid = (left+right)//2
        if A[mid] == B[i]:
            R = True
            print("1")
            break
        elif A[mid]>B[i]:
            right = mid-1
        else:
            left = mid+1
    if R == False:
        print("0")