import heapq
import sys

def cal(x):
    global answer
    if x > 0:
        heapq.heappush(hq, -x)

    if x == 0:
        if hq:
            answer.append(-heapq.heappop(hq))
        else:
            answer.append(0)        

N = int(input())
hq = []
answer = []

for _ in range(N):
    cal(int(sys.stdin.readline()))

for a in answer:
    sys.stdout.write(str(a) + '\n')