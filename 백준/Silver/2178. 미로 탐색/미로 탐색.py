import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):

    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
                
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[cx][cy] + 1
                q.append((nx, ny))


N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

count = 0
bfs(0, 0)

print(maze[N-1][M-1])