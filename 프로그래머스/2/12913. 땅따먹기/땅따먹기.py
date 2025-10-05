def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    
    scores = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if n == 0:
                scores[i][j] = land[i][j]
            else:
                temp = scores[i-1][:]
                del temp[j]
                scores[i][j] = max(temp) + land[i][j]
    
    return max(scores[-1])