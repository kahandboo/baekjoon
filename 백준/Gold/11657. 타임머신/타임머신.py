import sys

N, M = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, N+1)}
distance = [float('inf')] * (N+1)

for _ in range(M):
    a,b,c = map(int, sys.stdin.readline().split())

    graph[a].append((b,c))

distance[1] = 0

for _ in range(N - 1):
    for i in range(1, N+1):
        for j in graph[i]:
            v, w = j

            if distance[i] != float('inf') and distance[i] + w < distance[v]:
                distance[v] = distance[i] + w

for i in range(1,N+1):
    for j in graph[i]:
        v,w = j

        if distance[i] + w < distance[v]:
            print(-1)
            sys.exit()

for i in range(2, len(distance)):
    if distance[i] == float('inf'):
        sys.stdout.write(str(-1) + '\n')
    else:
        sys.stdout.write(str(distance[i]) + '\n')
        
