import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

city = []
home = []
chic = []
chicD = []
solve = 0
minnum = 1000000

for i in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))
for ind, i in enumerate(city):
    for ind2, j in enumerate(i):
        if j == 1:
            home.append([ind, ind2])
        elif j == 2:
            chic.append([ind, ind2])

chic = list(combinations(chic, M)) # 치킨집 리스트 목록
for k in chic: # 치킨집 경우의 수
    for i in home: # 집 목록 - 집에 따른 최솟값을 더해야되니까
        for j in k: # 한 가정에서 여러 치킨집까지의 거리를 구하는 식
            chicD.append(abs(i[0]-j[0]) + abs(i[1]-j[1])) # 한 가정에서 여러 치킨집까지의 거리가 들어가 있는 리스트
        solve += min(chicD)
        chicD.clear()
    if minnum > solve:
        minnum = solve
    solve = 0




print(minnum)