def solution(n):
    def getSubSum(i, j):
        if i == 0:
            return totsum[j]
        else:
            return totsum[j] - totsum[i-1]
    
    answer = 1
    tot = 0
    totsum = []
    
    for i in range(0, n):
        tot += i
        totsum.append(tot)
    
    left = 1
    right = 1
    
    while right < n:
        curr_val = getSubSum(left, right)
        
        if curr_val < n:
            right += 1
        elif curr_val > n:
            left += 1
        else:
            answer += 1
            left += 1
    return answer