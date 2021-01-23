priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    sol = list()
    loc = [priorities[location], location]
    print(loc)
    for i in range(len(priorities)):
        sol.append([priorities[i], i])
    sol = sorted(sol, key=lambda x:x[0], reverse=True)
    print(sol)
    return(sol.index(loc) + 1)

print(solution(priorities, location))