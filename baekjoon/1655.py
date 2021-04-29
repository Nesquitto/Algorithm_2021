import sys
import heapq

N = int(sys.stdin.readline().rstrip())
leftheap = list() # max
rightheap = list() # min
a = int(sys.stdin.readline().rstrip())
heapq.heappush(leftheap, (-a, a))
print(leftheap[0][1])
for i in range(N-1):
    num = int(sys.stdin.readline().rstrip())
    if len(leftheap) <= len(rightheap):
        heapq.heappush(leftheap, (-num, num))
    else:
        heapq.heappush(rightheap, (num, num))
    if leftheap[0][1] > rightheap[0][1]:
        a = heapq.heappop(leftheap)[1]
        b = heapq.heappop(rightheap)[1]
        heapq.heappush(rightheap, (a, a))
        heapq.heappush(leftheap, (-b, b))
    print(leftheap[0][1])
