import sys

def partsum(l, r):
    if l == 0:
        return sumlist[r]
    else:
        return sumlist[r] - sumlist[l-1]

N, target = map(int, sys.stdin.readline().split())
mylist = list(map(int, sys.stdin.readline().split()))
sumlist = []
n = 0

for i in mylist:
    n += i
    sumlist.append(n)

left = 0
right = 0
ans = float('inf')

while right < N and left <= right:

    temp = partsum(left, right)
    
    if temp >= target:
        if right-left+1 < ans:
            ans = right-left+1
        left += 1
    elif temp < target:
        right += 1

if ans == float('inf'):
    print(0)
else:
    print(ans)
