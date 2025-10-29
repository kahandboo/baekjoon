import sys
sys.setrecursionlimit(10**6)

N = int(input())

grid = [[' '] * N for _ in range(N)]

def drawStar(x, y, n):
    if n==1:
        grid[x][y] = '*'
        return
    else:
        size = n // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                drawStar(x+i*size, y+j*size, size)

drawStar(0, 0, N)

for row in grid:
    sys.stdout.write(''.join(row) + '\n')