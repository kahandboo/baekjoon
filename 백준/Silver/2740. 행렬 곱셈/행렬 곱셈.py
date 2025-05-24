import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())

for _ in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]


for i in range(N):
    for j in range(K):
        sys.stdout.write(str(result[i][j]) + ' ')
    sys.stdout.write('\n')