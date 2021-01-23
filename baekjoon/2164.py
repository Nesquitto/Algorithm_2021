import sys
import collections

N = int(sys.stdin.readline())

queue = collections.deque([i+1 for i in range(N)])
for i in range(N-1):
    queue.popleft()
    queue.append(queue.popleft())
print (queue[0])