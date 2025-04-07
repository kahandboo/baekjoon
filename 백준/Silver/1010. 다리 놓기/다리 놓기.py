import sys
import math

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())

    result.append(round(math.factorial(m)/(math.factorial(m-n if m-n !=0 else 1)*(math.factorial(n)))))

sys.stdout.write('\n'.join(map(str, result)) + '\n')