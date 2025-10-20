import sys

sys.setrecursionlimit(10**6)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

M, N = map(int, input().split())
parent = [0] * (M+1)

for i in range(1, M+1):
    parent[i] = i

answer = []

for _ in range(N):
    op, a, b = map(int, input().split())

    if (op == 0):
        union(a, b)
    else:
        if (find(a) == find(b)):
            answer.append('YES')
        else:
            answer.append('NO')

for ans in answer:
    print(ans)