def solution(s):
    answer = [0, 0] # 이진 변환 횟수, 제거된 0의 갯수
    while s is not "1":
        removed_s = s.replace("0", "")
        c = len(removed_s)
        
        answer[0] += 1
        answer[1] += len(s) - len(removed_s)
        
        s = bin(c)
        s = s[2:]
    
    return answer