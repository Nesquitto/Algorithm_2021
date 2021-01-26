def uc(X,Y):
    while(Y):
        X,Y = Y,X%Y
    return X
def uc2(X,Y):
    result = (X*Y) // uc(X,Y)
    return result

def solution(n, m):
    answer = []
    answer.append(uc(n,m), uc2(n,m))
    return answer    