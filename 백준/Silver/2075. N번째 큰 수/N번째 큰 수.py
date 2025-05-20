import heapq
import sys

def cal(x):
    for n in x:
        heapq.heappush(hq, n)

        if len(hq) > N:
            heapq.heappop(hq)
    

N = int(input())
hq = []

for _ in range(N):
    cal(map(int, sys.stdin.readline().split()))

print(heapq.heappop(hq))