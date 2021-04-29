import sys
import heapq

heap = list()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    com = int(sys.stdin.readline().rstrip())
    if com == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(com),com))
