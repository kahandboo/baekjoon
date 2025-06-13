import sys

V, E = map(int, sys.stdin.readline().split())
distance = [[float('inf')] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    
    if distance[a][b] > c:
        distance[a][b] = c

ans = float('inf')

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if i!=j and distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]


for i in range(1,V+1):
    for j in range(1,V+1):
        if i != j and distance[i][j] + distance[j][i] < ans:
            ans = distance[i][j] + distance[j][i]

if ans == float('inf'):
    print(-1)
else:
    print(ans)