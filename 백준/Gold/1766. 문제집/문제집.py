import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
result = []

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    indegree[b] += 1

q = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    u = heapq.heappop(q)
    result.append(u)
    
    if graph[u]:
        
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

for r in result:
    sys.stdout.write(str(r) + ' ')