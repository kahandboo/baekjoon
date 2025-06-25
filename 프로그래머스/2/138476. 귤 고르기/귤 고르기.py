def solution(k, tangerine):
    
    hashtable = {}
    
    for t in tangerine:
        
        if t in hashtable:
            hashtable[t] += 1
        else:
            hashtable[t] = 1
            
    sorted_dict = dict(sorted(hashtable.items(), key=lambda x: x[1], reverse=True))
    
    answer = 0
    target = 0
    
    for key, val in sorted_dict.items():
        target += val
        answer += 1
        
        if target >= k:
            break
    
    return answer