def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(idx, curr_sum):
        if idx == n:
            if curr_sum == target:
                nonlocal answer
                answer += 1
            return
        
        dfs(idx+1, curr_sum - numbers[idx])
        dfs(idx+1, curr_sum + numbers[idx])
    
    
    dfs(0, 0)
    return answer