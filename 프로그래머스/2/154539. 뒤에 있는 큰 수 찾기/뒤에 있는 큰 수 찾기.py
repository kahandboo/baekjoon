import copy
def solution(numbers):
    answer = []
    stack = []
    
    for i in range(len(numbers)-1, -1, -1):
        if not stack:
            answer.append(-1)
        else:
            while stack and stack[-1] <= numbers[i]:
                stack.pop()
            if not stack:
                answer.append(-1)
            else:
                answer.append(stack[-1])
            
        stack.append(numbers[i])


    return answer[::-1]