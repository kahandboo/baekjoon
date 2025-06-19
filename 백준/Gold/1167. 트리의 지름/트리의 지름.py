import sys
from collections import deque

def bfs(node):
    visited = [-1] * (V+1)

    q = deque()
    q.append(node)
    visited[node] = 0

    while q:
        now = q.popleft()
        for next, weight in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + weight
                q.append(next)

    dist = max(visited)
    n = visited.index(dist)
    return dist, n

V = int(sys.stdin.readline())
graph = {i : [] for i in range(1, V+1)}

for _ in range(V):
    mylist = list(map(int, sys.stdin.readline().split()))

    a = mylist[0]
    i=1

    while mylist[i] != -1:
        graph[a].append((mylist[i], mylist[i+1]))
        graph[mylist[i]].append((a, mylist[i+1]))
        i += 2

a_dist, a = bfs(1)
b_dist, b = bfs(a)

print(b_dist)