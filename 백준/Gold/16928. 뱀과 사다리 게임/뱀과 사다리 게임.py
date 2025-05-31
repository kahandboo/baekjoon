import sys
from collections import deque

def bfs():
    visited = [0] * 101
    q = deque([1])

    while q:
        c = q.popleft()
        
        if c == 100:
            return visited[c]
        
        for i in range(1,7):
            n = c + i

            if n > 100:
                continue

            if n in hash:
                n = hash[n]

            if visited[n] == 0:
                visited[n] = visited[c] + 1
                q.append(n)
                

N, M = map(int, sys.stdin.readline().split())

hash = {}

for _ in range(N+M):
    key, val = map(int, sys.stdin.readline().split())

    hash[key] = val



print(bfs())