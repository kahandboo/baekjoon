import sys
import heapq

t = int(input())

for _ in range(t):
    k = int(sys.stdin.readline())

    pages = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(pages)
    answer = 0

    while pages:
        x = heapq.heappop(pages)

        if not pages:
            print(answer)
            break

        y = heapq.heappop(pages)

        heapq.heappush(pages, x+y)
        answer += x+y
