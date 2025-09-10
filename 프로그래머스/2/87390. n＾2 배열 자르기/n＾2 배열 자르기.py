def solution(n, left, right):
    answer = []
    
    for k in range(left, right + 1):
        row, col = divmod(k, n) 
        answer.append(max(row, col) + 1)
    
    return answer