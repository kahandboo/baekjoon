import sys
import heapq

def dijkstra(n):
    q = []
    heapq.heappush(q, (0, n))

    distance = [10**9] * (N+1)
    distance[n] = 0

    while q:
        d, node = heapq.heappop(q)

        if d > distance[node]:
            continue

        for i in graph[node]:
            w, next = i
            nd = d + w
            if nd < distance[next]:
                distance[next] = nd
                heapq.heappush(q, (nd, next))
    
    return distance

result = []
T = int(sys.stdin.readline())
for _ in range(T):
    N,m,t = map(int, sys.stdin.readline().split())
    s,g,h = map(int, sys.stdin.readline().split())
    graph = { i: [] for i in range(1, N+1)}
    gh = 10**9
    
    for _ in range(m):
        a,b,d = map(int, sys.stdin.readline().split())
        
        graph[a].append((d,b))
        graph[b].append((d,a))

        if (a==g and b==h) or (a==h and b==g):
            gh = d

    r = []
    x = []

    for _ in range(t):
        x.append(int(sys.stdin.readline()))

    path1 = 0 # 출발지 -> g -> h 
    path2 = 0 # 출발지 -> h -> g 

    fromS = dijkstra(s)
    fromG = dijkstra(g)
    fromH = dijkstra(h)

    path1 = fromS[g] + gh
    path2 = fromS[h] + gh
    

    for i in x:
        if path1 + fromH[i] == fromS[i] or path2 + fromG[i] == fromS[i]:
            r.append(i)

    r.sort()
    result.append(r)

for res in result:
    for i in res:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')
