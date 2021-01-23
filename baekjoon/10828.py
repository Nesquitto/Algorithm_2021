import sys

N = int(sys.stdin.readline().rstrip())
comlist = list()
for i in range(N):
    Command= list(sys.stdin.readline().split())
    if(Command[0] == "push"):
        comlist.append(Command[1])
    elif(Command[0] == "pop"):
        if(len(comlist) > 0):
            print(comlist.pop(len(comlist)-1))
        else:
            print(-1)
    elif(Command[0] == "size"):
        print(len(comlist))
    elif(Command[0] == "empty"):
        if(len(comlist) == 0):
            print(1)
        else:
            print(0)
    else:
        if(len(comlist) > 0):
            print(comlist[len(comlist)-1])
        else:
            print(-1)