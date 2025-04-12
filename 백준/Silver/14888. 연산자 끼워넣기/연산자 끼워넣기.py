import sys

def calculate(index, a, b):
    if (index == 0):
        return a + b
    elif (index == 1):
        return a - b
    elif (index == 2):
        return a * b
    elif (index == 3):
        if a < 0:
            return -(abs(a)//b)
        else:
            return a//b

def backtrack(sum, i, op):
    if i == N :
        result.append(sum)
        return

    for index, val in enumerate(op):
        if val > 0:
            next_sum = calculate(index, sum, A[i])
            op[index] -= 1
            backtrack(next_sum, i+1, op)
            op[index] += 1
        else:
            continue

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operation = list(map(int, sys.stdin.readline().split()))

result = []
i = 1
sum = A[0]

backtrack(sum, i, operation)


sys.stdout.write(str(max(result)) + '\n')
sys.stdout.write(str(min(result)))
