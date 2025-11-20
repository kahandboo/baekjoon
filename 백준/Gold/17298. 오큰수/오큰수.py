N = int(input())
A = list(map(int, input().split()))

stack = []
answer = []

A.reverse()

for a in A:
    if not stack:
        answer.append(-1)
        stack.append(a)
    else:
        nge = 0
        popped_list = []
        while stack and stack[-1] <= a:
            popped = stack.pop()
            
            popped_list.append(popped)
        
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        
        stack.append(a)

print(*reversed(answer))