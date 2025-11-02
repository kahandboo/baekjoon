import sys

def dfs(graph, visited, node, parent):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            result = dfs(graph, visited, child, node)
            if not result:
                return False
        else:
            if child != parent:
                return False
    return True

answer = []

while True:
    n, m = map(int, sys.stdin.readline().split())
    if (n==0 and m==0): break

    graph = {i: [] for i in range(1, n+1)}

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())

        graph[a].append(b)
        graph[b].append(a)

    tree_count = 0
    visited = set()

    for i in range(1, n+1):
        if i in visited:
            continue
        if dfs(graph, visited, i, 0):
            tree_count += 1
    
    if tree_count == 1:
        answer.append("There is one tree.")
    elif tree_count > 1:
        answer.append(f"A forest of {tree_count} trees.")
    else:
        answer.append("No trees.")
    
for i in range(1, len(answer)+1):
    print(f"Case {i}: {answer[i-1]}")