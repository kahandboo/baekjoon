import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))

up = [1] * N
prev = [i for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            if up[i] < up[j] + 1:
                up[i] = up[j] + 1
                prev[i] = j
            else:
                up[i] = up[i]

max_val = max(up)
max_idx = up.index(max_val)

print(max_val)

cur_idx = max_idx
result = []

while prev[cur_idx] != cur_idx:
    result.append(A[cur_idx])
    cur_idx = prev[cur_idx]

result.append(A[cur_idx])
result.sort()
print(*result)