import sys
import heapq

V, E= map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = {i: [] for i in range(1, V+1)}
distance = {i: float('inf') for i in range(1, V+1)}
distance[K] = 0

q = []

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u].append((w, v))

heapq.heappush(q, (0, K))

while q:
    d, node = heapq.heappop(q)

    if d > distance[node]:
        continue

    for w, n in graph[node]:
        nd = d + w
        if nd < distance[n]:
            distance[n] = nd
            heapq.heappush(q, (nd, n))

for i in range(1, V+1):
    if distance[i] == float('inf'):
        sys.stdout.write('INF' + '\n')
    else:        
        sys.stdout.write(str(distance[i]) + '\n')