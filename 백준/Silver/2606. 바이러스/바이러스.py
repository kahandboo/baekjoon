import sys

def dfs(r):
    global count

    if r not in graph:
        count += 1
        visited[r] = True
        return        

    if not visited[r]:
        visited[r] = True
        count += 1

        for i in graph[r]:

            if not visited[i]:
                dfs(i)
    


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [False] * (N + 1)
graph = {}
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

dfs(1)

print(count - 1)