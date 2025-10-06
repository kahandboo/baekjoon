import heapq
def solution(n, works):
    answer = 0
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        if not works:
            break
            
        work = -heapq.heappop(works)
        work -= 1
        
        if work == 0:
            continue
        heapq.heappush(works, -work)
        
    while works:
        work = -heapq.heappop(works)
        answer += work**2
    
    return answer