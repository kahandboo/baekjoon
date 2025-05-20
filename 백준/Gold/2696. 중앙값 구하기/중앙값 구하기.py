import heapq
import sys

def cal(x):
  
    for n in range(len(x)):
        heapq.heappush(hq, x[n])
        
        if (n+1) % 2 == 1:
            copyhq = hq[:]
            for _ in range(((n+1)//2 + 1)):
                res = heapq.heappop(copyhq)

            templist.append(res)

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    M = int(sys.stdin.readline())
    hq = []
    templist = []
    inputlist = list(map(int, sys.stdin.readline().split()))

    for _ in range(1, M//10 + 1):
        inputlist.extend(list(map(int, sys.stdin.readline().split())))
    
    cal(inputlist)
    answer.append(templist)

for i in answer:
    sys.stdout.write(str(len(i)) + '\n')
    for j in range(len(i)):
        sys.stdout.write(str(i[j]) + ' ')
        if (j+1) % 10 == 0:
            sys.stdout.write('\n')
    sys.stdout.write('\n')
