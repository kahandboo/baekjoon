import re
def solution(s):
    answer = []
    s = s[1:-1]
    result = re.findall(r"\{[^}]*\}", s)
    result.sort(key=len)
    total = set()
    
    for r in result:
        r = r[1:-1]
        arr = list(map(int, r.split(',')))
        now = set(arr)
        
        val = list(now-total)
        
        answer.append(val[0])
        total |= now
    
    return answer