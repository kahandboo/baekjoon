import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
answer = []

q = deque(range(1, n+1), maxlen=n)

for _ in range(n):
    q.rotate(-(k-1))
    answer.append(q.popleft())

sys.stdout.write('<' + ', '.join(map(str, answer)) + '>\n')
