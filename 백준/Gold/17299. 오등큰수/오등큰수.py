from collections import deque
N = int(input())
A = list(map(int, input().split()))

count_dict = {}

for a in A:
    count_dict[a] = (count_dict.get(a) or 0) + 1

A.reverse()
stack = deque([])
answer = []

for a in A:
    if not stack:
        answer.append(-1)
        stack.append(a)
    else:    
        while stack and count_dict[stack[-1]] <= count_dict[a]:
            stack.pop()
        
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        stack.append(a)

print(*reversed(answer))