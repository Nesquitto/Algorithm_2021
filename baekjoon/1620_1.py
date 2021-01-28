# 이 문제는 input 대신 sys.stdin.readline() 을 사용해야 합니다.
a = list(map(int, input().split()))
b = []
c = []
for i in range(a[0]):
    b.append((i+1, input()))
c = b[:]
c.sort(key = lambda x:x[1])
for j in range(a[1]):
    pro = input()
    first = 0
    end = a[0]-1
    if pro.isdigit():
        print(b[int(pro)-1][1])
    else:
         while first <= end:
            mid = (end+first)//2
            if pro == c[mid][1]:
                print(c[mid][0])
                break
            elif pro < c[mid][1]:
                end = mid-1
            else:
                first = mid+1