import sys
from collections import deque

left = deque(sys.stdin.readline().rstrip())
right = deque()

for i in range(int(sys.stdin.readline().rstrip())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if len(left) >0:
            right.appendleft(left.pop())

    elif  command[0] == 'D':
        if len(right) > 0:
            left.append(right.popleft())

    elif command[0] == 'B':
        if len(left) > 0:
            left.pop()

    else:
        left.append(command[1])

print("".join(left),end="")
print("".join(right))