def solution(n, s):
    answer = []
    if s/n < 1:
        return [-1]
    
    for N in range(n, 0, -1):
        quotient = s // N
        s -= quotient
        
        answer.append(quotient)
        
    return answer