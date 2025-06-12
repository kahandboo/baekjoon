import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
distance = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0
    
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())

    if c < distance[a][b]:
        distance[a][b] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == float('inf'):
            sys.stdout.write(str(0) + ' ')
        else:
            sys.stdout.write(str(distance[i][j]) + ' ')
        
        if j == n:
            sys.stdout.write('\n')