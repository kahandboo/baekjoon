import sys, heapq
sys.setrecursionlimit(10**6)

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False
    
    if a < b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    return True

def getDistance(nx, ny, mx, my):
    return ((mx - nx) ** 2 + (my - ny) ** 2) ** 0.5

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
queue = []
grid = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    grid.append((x, y))

num_edges = 0
total_w = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1

    nx, ny = grid[a]
    mx, my = grid[b]
    distance = getDistance(nx, ny, mx, my)

    if union(a, b):
        num_edges += 1
    

for i in range(n - 1):
    for j in range(i+1, n):
        nx, ny = grid[i]
        mx, my = grid[j]
        distance = getDistance(nx, ny, mx, my)

        heapq.heappush(queue, (distance, i, j))


while num_edges < n-1:
    w, i, j = heapq.heappop(queue)

    if union(i, j):
        total_w += w
        num_edges += 1

print(f"{total_w:.2f}")