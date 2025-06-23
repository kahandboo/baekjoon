def solution(record):
    
    ans = []
    answer = []
    idToName = {}
    
    for r in record:
        if r[0] == 'E':
            action, uid, name = r.split()
            
            idToName[uid] = name
            
            ans.append((uid, 'E'))
            
        elif r[0] == 'L':
            action, uid = r.split()
            
            ans.append((uid, 'L'))
        else: 
            action, uid, name = r.split()
            idToName[uid] = name
    
    for a in ans:
        curr_uid, act = a
        
        if act == 'E':
            answer.append(idToName[curr_uid] + '님이 들어왔습니다.')
        else:
            answer.append(idToName[curr_uid] + '님이 나갔습니다.')
    
    
    return answer