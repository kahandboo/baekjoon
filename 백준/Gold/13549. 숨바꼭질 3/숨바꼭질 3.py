import sys
import heapq



N, K = map(int, sys.stdin.readline().split())

distance = { i: float('inf') for i in range(0, 10**5 + 1)}
distance[N] = 0

q = []
heapq.heappush(q, (0, N))

while q:
    d, n = heapq.heappop(q)

    if d > distance[n]:
        continue
    
    if 0 <= n-1 <= 10**5 and d + 1 < distance[n-1]:
        distance[n-1] = d + 1
        heapq.heappush(q, (d+1, n-1))
    if 0 <= n+1 <= 10**5 and d + 1 < distance[n+1]:
        distance[n+1] = d + 1
        heapq.heappush(q, (d+1, n+1))
    if 0 <= n*2 <= 10**5 and d < distance[n*2]:
        distance[n*2] = d
        heapq.heappush(q, (d, n*2))

print(distance[K])