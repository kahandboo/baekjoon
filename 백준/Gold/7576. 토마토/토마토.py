import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if box[nx][ny] == -1:
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx,ny))

M, N = map(int, sys.stdin.readline().split())
box = []
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

answer = []
visited = [[-1] * M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = 0
            q.append((i,j))

bfs()
count = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 0 and visited[i][j] == -1:
            print(-1)
            sys.exit()
        count = max(count, visited[i][j])

print(count)

