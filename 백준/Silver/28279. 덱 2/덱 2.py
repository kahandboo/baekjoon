import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()
answer = []

for _ in range(n):
    val = sys.stdin.readline().split()
    op = int(val[0])
    num = int(val[1]) if len(val) > 1 else 0

    if (op == 1):
        dq.appendleft(num)
    elif (op == 2):
        dq.append(num)
    elif (op == 3):
        if dq:
            answer.append(dq.popleft())
        else:
            answer.append(-1)
    elif (op == 4):
        if dq:
            answer.append(dq.pop())
        else:
            answer.append(-1)
    elif (op == 5):
        answer.append(len(dq))
    elif (op == 6):
        answer.append(1) if len(dq) == 0 else answer.append(0)
    elif (op == 7):
        if dq:
            answer.append(dq[0])
        else:
            answer.append(-1)
    elif (op == 8):
        if dq:
            answer.append(dq[-1])
        else:
            answer.append(-1)


sys.stdout.write('\n'.join(map(str, answer))+'\n')