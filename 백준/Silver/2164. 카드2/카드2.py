import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque(range(1, n+1))

for _ in range(n-1):
    q.popleft()
    q.rotate(-1)

print(q.pop())