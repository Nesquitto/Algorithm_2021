import sys

res = 0
N = int(sys.stdin.readline().rstrip())

def solve(n, size, depth, num):
    global res
    iscon = False
    size.append(num)

    if len(size) == n:
        res +=1
        return 0
    else:
        for i in range(n): # 후보위치
            if i in size: # 같은 열에 있는지 확인
                continue
            for j in range(1, depth+1): # 윗줄을 확인
                if size[depth-j] == i-j or size[depth-j] == i+j:
                    iscon = True
                    break
            if iscon:
                iscon = False
                continue
            solve(N, size[:], depth+1, i)
                


for i in range(N):
    solve(N, [], 1, i)
print(res)