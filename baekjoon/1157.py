st = input()
st = st.upper()
a = []
b = [0 for i in range(30)]
c = []
for i in range(len(st)):
    if st[i] not in a:
        a.append(st[i])
    b[a.index(st[i])] = b[a.index(st[i])] + 1

for i in range(len(b)):
    if b[i] == max(b):
        c.append(i)
if len(c)== 1:
    print(a[c[0]])
else:
    print("?")

