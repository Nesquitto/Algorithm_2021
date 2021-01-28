import sys
ipAddr = list(sys.stdin.readline().rstrip().split(':'))
le = 0
arr = [''for i in range(8)]
isthat = True
for i in range(len(ipAddr)):
    a = True
    if len(ipAddr[i]) == 4:
        arr[le] = ipAddr[i]
        le += 1
    elif len(ipAddr[i])>0:
        arr[le] = '0' * (4-len(ipAddr[i])) + ipAddr[i]
        le += 1
    else:
        if isthat:
            isthat = False
            for j in range(8-len(ipAddr)+1):
                arr[le] = '0000'
                le += 1
        else:
            arr[le] = '0000'
            le += 1
for i in range(len(arr)):
    if i != len(arr)-1:
        print(arr[i], end=':')
    else:
        print(arr[i], end='')
