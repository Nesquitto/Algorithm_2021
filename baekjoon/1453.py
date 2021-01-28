num = int(input())
ret = 0
seat = [False for i in range(100)]
per = list(map(int, input().split()))
for i in range(num):
    if seat[per[i]-1] == True:
        ret = ret+1
    seat[per[i]-1] = True
print (ret)
