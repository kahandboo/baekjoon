import sys
import heapq

def dijkstra(n):
    distance = {i: float("inf") for i in range(1, N+1)} 
    distance[n] = 0

    q = []

    heapq.heappush(q, (0, n))

    while q:
        d, node = heapq.heappop(q)

        if d > distance[node]:
            continue

        for w, n in graph[node]:
            nd = d + w
            if nd < distance[n]:
                distance[n] = nd
                heapq.heappush(q, (nd, n))
    
    return distance
    

N, E = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().split())

from1 = dijkstra(1)
fromv1 = dijkstra(v1)
fromv2 = dijkstra(v2)

path1 = from1[v1] + fromv1[v2] + fromv2[N]
path2 = from1[v2] + fromv2[v1] + fromv1[N]

if path1 == float('inf') or path2 == float('inf'):
    print(-1)
else:
    print(min(path1, path2))