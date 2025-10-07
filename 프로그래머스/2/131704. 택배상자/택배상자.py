def solution(order):
    answer = 0
    stack = []
    j = 0
    
    for i in range(1, len(order) + 1):
        if i == order[j]:
            answer += 1
            j += 1
            while stack and stack[-1] == order[j]:
                stack.pop()
                answer += 1
                j += 1
        else:
            stack.append(i)
    
    return answer