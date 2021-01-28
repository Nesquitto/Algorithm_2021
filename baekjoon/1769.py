a = input()
count = 0
while(len(a) != 1):
    b = 0
    for i in range(len(a)):
        b = b + int(a[i])
    a = str(b)
    count = count + 1
print(count)
if(int(a)%3==0):
    print("YES")
else:
    print("NO")
