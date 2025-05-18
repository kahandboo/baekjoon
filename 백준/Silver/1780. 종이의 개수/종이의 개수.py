import sys

white = 0
blue = 0
red = 0

def f(grid):
    global white, blue, red
    n = len(grid)

    if n == 1:
        if grid[0][0] == 0:
            white += 1
        elif grid[0][0] == 1:
            blue += 1
        else:
            red += 1
        return

    if sum(row.count(0) for row in grid) == n ** 2:
        white += 1
        return
    elif sum(row.count(1) for row in grid) == n ** 2:
        blue += 1
        return
    elif sum(row.count(-1) for row in grid) == n ** 2:
        red += 1
        return
    
    third = n // 3
    half = third * 2

    f([row[0:third] for row in grid[0:third]])
    f([row[0:third] for row in grid[third:half]])
    f([row[0:third] for row in grid[half:n]])

    f([row[third:half] for row in grid[0:third]])
    f([row[third:half] for row in grid[third:half]])
    f([row[third:half] for row in grid[half:n]])

    f([row[half:n] for row in grid[0:third]])
    f([row[half:n] for row in grid[third:half]])
    f([row[half:n] for row in grid[half:n]])
    

N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

f(grid)

print(red)
print(white)
print(blue)
