import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

up = [1] * N
down = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            up[i] = max(up[i], up[j] + 1)

for i in range(N-1, -1, -1):
    for k in range(N-1, i, -1):
        if A[k] < A[i]:
            down[i] = max(down[i], down[k] + 1)
        

print(max(up[i] + down[i] - 1 for i in range(N)))