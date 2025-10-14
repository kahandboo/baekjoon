def solution(A, B):
    answer = 0
    B.sort()
    A.sort()
    b_idx = 0 
    
    for a_num in A:
        while b_idx < len(B) and B[b_idx] <= a_num:
            b_idx += 1
            
        
        if b_idx < len(B):
            answer += 1
            
            b_idx += 1 
    
    return answer