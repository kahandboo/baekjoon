import sys

texts = []

while True:
    line = input()
    if line == '.':
        break
    texts.append(line)
    
answer = []
hash = {')':'(', ']':'['}

for text in texts:
    stack = []

    for i in text:
        if not stack: 
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')' or i == ']':
                answer.append('no')
                stack.append('no')
                break
        else:
            if i in hash:
                if stack[-1] == hash[i]:
                    stack.pop()
                else:
                    stack.append('no')
                    answer.append('no')
                    break
            else:
                if i =='(' or i == '[':
                    stack.append(i)

    if not stack:
        answer.append('yes')
    elif stack[-1] == '[' or stack[-1] == ']' or stack[-1] == '(' or stack[-1] == ')':
        answer.append('no')
    

for a in answer:
    sys.stdout.write(a + '\n')

