import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
comdeq = deque()

for i in range(N):
    Command= list(sys.stdin.readline().split())
    if(Command[0] == "push_front"):
        comdeq.appendleft(Command[1])
    elif(Command[0] == "push_back"):
        comdeq.append(Command[1])
    elif(Command[0] == "pop_front"):
        if(len(comdeq) > 0):
            print(comdeq.popleft())
        else:
            print(-1)
    elif(Command[0] == "pop_back"):
        if(len(comdeq) > 0):
            print(comdeq.pop())
        else:
            print(-1)
    elif(Command[0] == "size"):
        print(len(comdeq))
    elif(Command[0] == "empty"):
        if(len(comdeq) == 0):
            print(1)
        else:
            print(0)
    elif(Command[0] == "front"):
        if(len(comdeq) > 0):
            print(comdeq[0])
        else:
            print(-1)
    else:
        if(len(comdeq) > 0):
            print(comdeq[len(comdeq)-1])
        else:
            print(-1)