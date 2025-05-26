import sys
sys.setrecursionlimit(10**6)

def dfs(r):
    global count

    visited[r] = True
    result[r] = count
    count += 1

    if r in graph:
        
        graph[r].sort()

        for i in graph[r]:

            if not visited[i]:
                dfs(i)


N, M, R = map(int, sys.stdin.readline().split())
graph = {}
result = [0] * (N+1)
visited = [False] * (N+1)
count = 1

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

    
dfs(R)

for i in range(1, N+1):
    sys.stdout.write(str(result[i]) + '\n')