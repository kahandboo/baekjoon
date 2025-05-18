import sys

def f(grid):
    n = len(grid)

    if n == 1:
        if grid[0][0] == 0:
            return '0'
        else:
            return '1'

    if sum(row.count(0) for row in grid) == n ** 2:
        return '0'
    elif sum(row.count(1) for row in grid) == n ** 2:
        return '1'
    
    half = n // 2

    ans = '(' + f([row[0:half] for row in grid[0:half]]) + f([row[half:n] for row in grid[0:half]]) + f([row[0:half] for row in grid[half:n]]) + f([row[half:n] for row in grid[half:n]]) +')'

    return ans


N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip())))

print(f(grid))


