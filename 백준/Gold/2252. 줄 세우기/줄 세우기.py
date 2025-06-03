import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    indegree[b] += 1

q = deque([])

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    n = q.popleft()
    result.append(n)

    for i in graph[n]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

for r in result:
    sys.stdout.write(str(r) + ' ')