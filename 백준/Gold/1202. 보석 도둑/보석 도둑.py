import heapq, sys

def cal(c):

    global idx

    while idx < N and gem[idx][0] <= c:
        heapq.heappush(hq, -gem[idx][1])  
        idx += 1

    if hq:
        return -heapq.heappop(hq)
    else:
        return 0
        

N, K = map(int, sys.stdin.readline().split())
bags = []
cost = 0
idx = 0
hq = []
gem = []


for _ in range(N):
    M, V =map(int, sys.stdin.readline().split())
    gem.append((M, V))

for _ in range(K):
    bags.append(int(sys.stdin.readline()))

gem.sort()
bags.sort()

for bag in bags:
    cost += cal(bag)

print(cost)