import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M_len = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))


dq = deque()

result = []

for i in range(N):
    if A[i] == 0:
        dq.append(B[i])


for j in range(M_len):
    dq.appendleft(M[j])
    result.append(dq.pop())

sys.stdout.write(' '.join(map(str, result)))