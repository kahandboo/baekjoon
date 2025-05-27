import sys
from collections import deque

def bfs(r):
    global count
    
    if r in graph:
        for i in graph[r]:
            visited[i] = False
    
    visited[r] = True
    result[r] = count
    count += 1

    q = deque([r])

    while q:
        u = q.popleft()
        result[u] = count
        count += 1
        
        if u in graph:
            graph[u].sort(reverse=True)

            for i in graph[u]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)


N, M, R = map(int, sys.stdin.readline().split())

graph = {}
visited = [0] * (N+1)
result = [0] * (N+1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]

    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

bfs(R)

for i in range(1, N+1):
    sys.stdout.write(str(result[i]) + '\n')

