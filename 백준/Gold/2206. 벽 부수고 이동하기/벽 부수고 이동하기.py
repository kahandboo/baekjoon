import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        cx, cy, b = q.popleft()

        for i in range(4):

            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if grid[nx][ny] == 1 and b == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = visited[cx][cy][0] + 1
                q.append((nx,ny,1))
            elif not visited[nx][ny][b] and grid[nx][ny] == 0:
                visited[nx][ny][b] = visited[cx][cy][b] + 1
                q.append((nx,ny,b))
        

N, M = map(int, sys.stdin.readline().split())
grid = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip())))

q = deque([(0,0,0)])
bfs()

if visited[N-1][M-1][0] == 0 and visited[N-1][M-1][1] == 0:
    print(-1)
elif visited[N-1][M-1][0] == 0:
    print(visited[N-1][M-1][1])
elif visited[N-1][M-1][1] == 0:
    print(visited[N-1][M-1][0])
else:
    print(min(visited[N-1][M-1][0], visited[N-1][M-1][1]))
