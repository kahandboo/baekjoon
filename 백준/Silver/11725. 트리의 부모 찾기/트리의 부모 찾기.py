import sys
from collections import deque

def bfs(n):
    q = deque([n])

    while q:
        curr = q.popleft()
        visited[curr] = True

        for child in tree[curr]:
            if not visited[child]:
                ans[child] = curr
                q.append(child)


N = int(sys.stdin.readline())
tree = [[] for i in range(N+1)]
ans = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(N-1):
    key, val = map(int, sys.stdin.readline().split())

    tree[key].append(val)
    tree[val].append(key)

bfs(1)

for i in range(2, len(ans)):
    sys.stdout.write(str(ans[i]) + '\n')