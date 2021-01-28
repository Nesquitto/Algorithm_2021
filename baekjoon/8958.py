T = int(input())
for i in range(T):
    count = 0
    sum = 0
    str = input()
    for j in range(len(str)):
        if str[j] == 'O':
            count = count +1
            sum = sum + count
        else:
            count = 0
    print(sum)