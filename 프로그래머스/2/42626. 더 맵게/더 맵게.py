import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        min_num1 = heapq.heappop(scoville)
        if (min_num1 >= K):
            return answer
        
        if not scoville:
            return -1
            
        min_num2 = heapq.heappop(scoville)
        
        new_scoville = min_num1 + (min_num2 * 2)      
        
        heapq.heappush(scoville, new_scoville)
        answer += 1
        
    
    return -1 if answer == 0 else answer