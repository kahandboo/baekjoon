import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    F = int(input())
    parent = {}
    size = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a
            size[a] += size[b]
        return size[a]

    for _ in range(F):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        result.append(union(a, b))

for r in result:
    print(r)