a = list(map(int, input().split()))
for i in range(a[2]):
    a[0] = a[0] % a[1] # 나머지를 구해서
    a[0] = a[0] * 10 # 소수점 n째자리 위치를 1의자리 위치로 옮기고
    ans = a[0] / a[1] # 나눠주게 되면 그 자리수의 값이 나온다
print(int(ans))

