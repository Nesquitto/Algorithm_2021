import sys
import heapq

N = int(sys.stdin.readline().rstrip())
data = list()
for i in range(N):
    data.append(int(sys.stdin.readline().rstrip()))
res = 0
heapq.heapify(data)
while(len(data) != 1):
    a = heapq.heappop(data)
    a += heapq.heappop(data)
    res += a
    heapq.heappush(data, a)
print(res)