import sys

n = int(sys.stdin.readline())
stack = []
answer = []

for _ in range(n):
    val = sys.stdin.readline().split()
    op = int(val[0])
    num = int(val[1]) if len(val) > 1 else 0

    if (op == 1):
        stack.append(num)
    elif (op == 2):
        if (len(stack) > 0):
            answer.append(str(stack.pop()))
        else:
            answer.append((-1))
    elif (op == 3):
        answer.append(str(len(stack)))
    elif (op == 4):
        answer.append(str(1 if len(stack) == 0 else 0))
    else:
        if (len(stack) == 0):
            answer.append(str(-1))
        else:
            answer.append(str(stack[-1]))

for i in answer:
    print(i)