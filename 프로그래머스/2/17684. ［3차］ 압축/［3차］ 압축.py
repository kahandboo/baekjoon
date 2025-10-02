def solution(msg):
    alphabet = {chr(i):i-64 for i in range(65, 91)}
    answer = []
    i = 0
    
    while i < len(msg):
        start = i
        end = i + 1
        for j in range(i, len(msg)+1):
            temp = msg[i:j]
            
            if temp in alphabet:
                start = i
                end = j 
                
        last_key = list(alphabet.keys())[-1]
        last_val = alphabet[last_key]
        i = end      
        
        if msg[start:end] not in alphabet:
            alphabet[msg[start:end]] = last_val + 1
            last_val += 1
        
        print(msg[start:end])
        answer.append(alphabet[msg[start:end]])
        
        if end < len(msg):
            alphabet[msg[start:end+1]] = last_val + 1
    
    return answer