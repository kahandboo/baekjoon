import sys

sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    if x < 0 or x >= M or y < 0 or y >= N:
        return 
    
    if graph[x][y] == 0:
        return 
    
    graph[x][y] = 0
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        dfs(nx, ny)
    
    return

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())

        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1


    answer.append(count)

for i in answer:
    sys.stdout.write(str(i) + '\n')