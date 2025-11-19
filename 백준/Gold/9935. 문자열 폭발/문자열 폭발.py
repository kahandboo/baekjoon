str = input()
bomb_str = input()
stack = []

answer = "FRULA"

for s in str:
    stack.append(s)

    if bomb_str[-1] == stack[-1]:
        temp = []
        match = True
        for s in reversed(bomb_str):
            if not stack:
                break

            temp.append(stack.pop())

            if s != temp[-1]:
                match = False
        
        if match == False or len(temp) != len(bomb_str):
            for c in reversed(temp):
                stack.append(c)

if not stack:
    print(answer)
else:
    print(''.join(stack))