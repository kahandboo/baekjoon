import sys

n = int(sys.stdin.readline())
answer = []

for _ in range(n):
    stack = []
    data = list(sys.stdin.readline())
    data.pop()

    for i in data:
        if (len(stack) > 0):
            if (stack[-1] == '(' and i == ')'):
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if (len(stack) == 0):
        answer.append('YES') 
    else: answer.append('NO')


sys.stdout.write('\n'.join(answer)+'\n')
        
    
    
