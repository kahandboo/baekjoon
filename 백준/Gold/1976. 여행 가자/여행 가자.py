import sys
sys.setrecursionlimit(10**6)

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

N = int(input())
M = int(input())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))

root = find(plan[0])

for i in range(1, M):
    if root != find(plan[i]):
        print('NO')
        sys.exit()

print('YES')