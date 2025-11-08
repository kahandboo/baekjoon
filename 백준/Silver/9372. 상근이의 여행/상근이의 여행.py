import sys

def kruskal(graph, parent):
    def find(n):
        if parent[n] == n:
            return n
        parent[n] = find(parent[n])
        return parent[n]
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            parent[root_a] = root_b
            return True
        return False
    
    mst_edges = []
    num_edges = 0

    for u in range(len(graph)):
        for v in graph[u]:
            if union(u, v):
                mst_edges.append((u,v))
                num_edges += 1
                if num_edges == len(graph) - 1:
                    break
        if num_edges == len(graph) - 1:
            break

    return len(mst_edges)
    
T = int(sys.stdin.readline())
result = []

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    parent = list(range(N+1))

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        
        graph[a].append(b)
        graph[b].append(a)
        
    result.append(kruskal(graph, parent))

for r in result:
    sys.stdout.write(str(r) + '\n')