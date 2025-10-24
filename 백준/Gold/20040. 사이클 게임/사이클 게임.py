import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if (a==b):
        return True

    if a<b:
        parent[b] = a
    else:
        parent[a] = b
    return False

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

n, m = map(int, input().split())
parent = []
ans = 0

parent = [i for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    if union(a, b) and ans == 0:
        ans = i+1


print(ans)


