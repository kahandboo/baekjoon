import sys
from collections import deque

def dfs(r):

    if r not in graph:
        result_dfs.append(r)
        visited[r] = True
        return        

    if not visited[r]:
        visited[r] = True
        result_dfs.append(r)

        graph[r].sort()

        for i in graph[r]:

            if not visited[i]:
                dfs(i)

def bfs(r):

    if r not in graph:
        result_bfs.append(r)
        visited[r] = True
        return
    
    if not visited[r]:
        
        q = deque([r])

        while q:
            u = q.popleft()
            if not visited[u]:
                visited[u] = True
                result_bfs.append(u)

            if u in graph:

                graph[u].sort()

                for i in graph[u]:
                    if not visited[i]:
                        q.append(i)
    


N, M, V = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
graph = {}
result_dfs = []
result_bfs = []

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

dfs(V)
visited = [False] * (N + 1)
bfs(V)

for i in result_dfs:
    sys.stdout.write(str(i) + ' ')

sys.stdout.write('\n')

for i in result_bfs:
    sys.stdout.write(str(i) + ' ')
