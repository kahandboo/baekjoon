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
    
    parent[root_b] = root_a
    return True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    parent = [i for i in range(m+1)]
    graph = []
    money = 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        money += z
        heapq.heappush(graph, (z, x, y))

    save_money = 0
    num_edges = 0

    while num_edges < m-1:
        z, x, y = heapq.heappop(graph)

        if union(x, y):
            save_money += z
            num_edges += 1
    
    sys.stdout.write(str(money - save_money) + '\n')