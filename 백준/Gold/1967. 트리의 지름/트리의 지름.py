import sys
from collections import deque

def dfs(node):
    visited = [-1] * (n+1)

    q = deque()
    q.append(node)
    visited[node] = 0

    while q:
        now = q.popleft()

        for next, weight in tree[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + weight
                q.append(next)

    return max(visited), visited.index(max(visited))
    


n = int(sys.stdin.readline())
tree = {i:[] for i in range(1, n+1)}

for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().split())

    tree[a].append((b,w))
    tree[b].append((a,w))

m, idx = dfs(1)
ans, i = dfs(idx)

print(ans)