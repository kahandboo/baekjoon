import sys
from collections import deque

n = int(sys.stdin.readline())
answer = []
queue = deque()

for _ in range(n):

    val = sys.stdin.readline().split()
    op = val[0]
    num = int(val[1]) if len(val) > 1 else 0

    if (op == 'push'):
        queue.append(num)
    elif (op == 'pop'):
        answer.append(str(queue.popleft())) if len(queue) > 0 else answer.append('-1')
    elif (op == 'size'):
        answer.append(str(len(queue)))
    elif (op == 'empty'):
        answer.append('0') if len(queue) != 0 else answer.append('1')
    elif (op == 'front'):
        if len(queue) > 0:
            answer.append(str(queue[0]))
        else:
            answer.append('-1')
    else:
        if len(queue) > 0:
            answer.append(str(queue[-1]))
        else:
            answer.append('-1')

sys.stdout.write('\n'.join(answer) + '\n')
            

