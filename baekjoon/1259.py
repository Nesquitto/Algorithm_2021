while(True):
    res = True
    a = input()
    if a == '0':
        break
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            res = False
    if res == True:
        print("yes")
    else:
        print("no")