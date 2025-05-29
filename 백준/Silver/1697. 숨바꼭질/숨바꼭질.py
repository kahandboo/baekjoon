import sys
from collections import deque

du = [1, -1, 2]

def bfs(n):
    q = deque([n])

    while q:
        u = q.popleft()

        for i in range(3):
            if i == 2:
                nu = u*du[i]
            else:
                nu = u + du[i]

            if nu < 0 or nu >= 100001:
                continue
            
            if visited[nu] == 0:
                visited[nu] = visited[u] + 1
                q.append(nu)

                if nu == K:
                    return


N, K = map(int, sys.stdin.readline().split())

visited = [0] * 100001

bfs(N)

if N == K:
    print(0)
else:
    print(visited[K])