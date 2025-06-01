import sys
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while q:
        ci, cj, ck = q.popleft()

        for i in range(6):
            ni = ci + dz[i]
            nj = cj + dy[i]
            nk = ck + dx[i]

            if nj < 0 or ni < 0 or nk < 0 or ni > H-1 or nj > N-1 or nk > M-1:
                continue

            if grid[ni][nj][nk] == -1:
                continue

            if visited[ni][nj][nk] == -1:
                visited[ni][nj][nk] = visited[ci][cj][ck] + 1
                q.append((ni,nj,nk))

M, N, H = map(int, sys.stdin.readline().split())
grid = []

visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().split())))
    grid.append(box)

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 1:
                visited[i][j][k] = 0
                q.append((i,j,k))

bfs()
count = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 0 and visited[i][j][k] == -1:
                print(-1)
                sys.exit()
            count = max(count, visited[i][j][k])

print(count)
