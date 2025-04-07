import sys
from collections import deque

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ballon = deque((i+1, num) for i, num in enumerate(nums))
result = []

for _ in range(n):
    idx, val = ballon.popleft()
    result.append(idx)

    if (val > 0):
        ballon.rotate(-(val - 1))
    else: 
        ballon.rotate(-val)

sys.stdout.write(' '.join(map(str, result)) + ' ')