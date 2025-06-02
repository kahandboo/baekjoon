import sys
sys.setrecursionlimit(10**6)

def dfs(v, color):
    if visited[v] == 0:
        visited[v] = color

        if v in graph:
            for n in graph[v]:
                if visited[n] == 0:
                    if not dfs(n, -color):
                        return False
                elif visited[n] == color:
                    return False
            return True
        else:
            return True
    else:
        return True
        
K = int(sys.stdin.readline())
answer = []

for i in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = {}
    visited = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())

        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]

        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]

    
    for v in range(1, V+1):
        if not dfs(v, 1):
            answer.append('NO')
            break
    else:
        answer.append('YES')

for ans in answer:
    sys.stdout.write(str(ans) + '\n')
