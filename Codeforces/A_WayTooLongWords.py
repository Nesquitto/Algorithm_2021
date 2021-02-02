import sys

for i in range(int(sys.stdin.readline().rstrip())):
    word = sys.stdin.readline().rstrip()
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[len(word)-1])
    else:
        print(word)