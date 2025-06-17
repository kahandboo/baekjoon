import math

def solution(progresses, speeds):
    
    n = len(progresses)
    remain = []
    
    for i in range(n):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))
    
    cutline = remain[0]
    count = 0
    ans = []
    
    for i in range(n):
        
        re = remain[i]
        
        if re <= cutline:
            count += 1
            
            if i == n-1:
                ans.append(count)
                
        else:
            ans.append(count)
            cutline = re
            count = 1
            
            if i == n-1:
                ans.append(count)
            
            
    return ans
                