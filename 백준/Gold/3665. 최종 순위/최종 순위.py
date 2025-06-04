import sys
from collections import deque

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            graph[t[i]].append(t[j])
            indegree[t[j]] += 1

    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())

        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1

    q = deque([])

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        if len(q) > 1:
            answer.append('?')
            break
        u = q.popleft()
        result.append(u)

        if graph[u]:
            for i in graph[u]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)
    else:
        if len(result) == n:
            answer.append(' '.join(map(str, result)))
        else:
            answer.append('IMPOSSIBLE')

for ans in answer:
    sys.stdout.write(str(ans) + '\n')