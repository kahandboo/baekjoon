import sys

white = 0
blue = 0

def f(grid):
    global white, blue
    n = len(grid)

    if n == 1:
        if grid[0][0] == 0:
            white += 1
        else:
            blue += 1
        return

    if sum(row.count(0) for row in grid) == n ** 2:
        white += 1
        return
    elif sum(row.count(1) for row in grid) == n ** 2:
        blue += 1
        return
    
    half = n // 2

    f([row[0:half] for row in grid[0:half]])

    f([row[half:n] for row in grid[0:half]])

    f([row[0:half] for row in grid[half:n]])

    f([row[half:n] for row in grid[half:n]])
    

N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

f(grid)

print(white)
print(blue)
