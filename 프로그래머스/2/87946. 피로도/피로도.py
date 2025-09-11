def solution(k, dungeons):
    def check(hp_now, visited, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            hp_need, hp_wasted = dungeons[i] 
            
            if hp_now < hp_need:
                continue
            
            if not visited[i]:  
                visited[i] = True
                
                check(hp_now - hp_wasted, visited, count+1)
                
                visited[i] = False


    visited = [False] * len(dungeons)    
    answer = 0    
    
    check(k, visited, 0)
        
    
    return answer