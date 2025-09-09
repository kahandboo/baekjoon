def solution(s):
    answer = 0
    dict = {
        '{':'}', '[':']', '(':')'
    }
    
    for i in range(len(s)):
        stack = []
        rotated = s[i:] + s[:i]
        
        for i in range(len(rotated)):
            brace = rotated[i]
            if brace in dict:
                stack.append(brace)
            else:
                if stack:
                    if stack[-1] in dict and dict[stack[-1]] == brace:
                        stack.pop()
                    else:
                        stack.append(brace)
                else:
                    stack.append(brace)
                    
        if not stack:
            answer += 1
    
    return answer