import sys

M = int(input())
S = 0

def runOp(op, num, S):
    if (op == 'add'):
        S = S | (1 << num)
    elif (op == 'remove'):
        S = S & ~(1 << num)
    elif (op == 'check'):
        if S & (1 << num):
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')
    elif (op == 'toggle'):
        S = S ^ (1 << num)
    elif (op == 'all'):
        S = (1 << 21) - 1
    else:
        S = 0
    
    return S

for _ in range(M):
    string = list(sys.stdin.readline().split())

    if len(string) > 1:
        op, x = string[0], int(string[1])
    else:
        op = string[0]
        x = 0

    S = runOp(op, x, S)
