import sys     

N, M = map(int, sys.stdin.readline().split())
grid = []
answer = []
prefix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer.append(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])


for ans in answer:
    sys.stdout.write(str(ans) + '\n')