import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, input().split())))

prev = 0
for i in range(M):
    maze[0][i] += prev
    prev = maze[0][i]

prev = 0
for i in range(N):
    maze[i][0] += prev
    prev = maze[i][0]

for i in range(1, N):
    for j in range(1, M):
        maze[i][j] += max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])

print(maze[N-1][M-1])