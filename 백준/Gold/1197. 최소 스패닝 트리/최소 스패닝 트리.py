import sys, heapq
sys.setrecursionlimit(10**6)

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False
    
    if a < b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    return True


V, E = map(int, sys.stdin.readline().split())

parent = [i for i in range(V+1)]
queue = []

for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())

    heapq.heappush(queue, (w, v1, v2))

num_edges = 0
total_w = 0

while num_edges < V-1:
    w, v1, v2 = heapq.heappop(queue)

    if union(v1, v2):
        num_edges += 1
        total_w += w

sys.stdout.write(str(total_w))