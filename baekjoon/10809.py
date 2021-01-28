alpha = [-1 for i in range(26)]
a = input()
for i in range(len(a)):
    if alpha[ord(a[i]) - 97] == -1:
        alpha[ord(a[i]) - 97] = i
for i in range(len(alpha)):
    print(alpha[i], end = " ")