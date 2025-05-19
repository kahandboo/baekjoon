import heapq
import sys

def cal(x):
    global answer
    if x < 0:
        heapq.heappush(hq, (abs(x), 0))
    elif x > 0:
        heapq.heappush(hq, (abs(x), 1))
    else:
        if hq:
            rs = heapq.heappop(hq)
            if rs[1] == 0:
                answer.append(-rs[0])
            else:
                answer.append(rs[0])
        else:
            answer.append(0)        

N = int(input())
hq = []
answer = []

for _ in range(N):
    cal(int(sys.stdin.readline()))

for a in answer:
    sys.stdout.write(str(a) + '\n')