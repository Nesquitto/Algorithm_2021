def solution(prices):
    li = []
    for i in range(len(prices)-1):
        sec= 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                sec = sec+1
            else:
                sec = sec+1
                break
        li.append(sec)
    li.append(0)
    return li