import sys
from bisect import bisect_right, bisect_left
from itertools import combinations

def com(arr):
    n = len(arr)
    result = []

    for i in range(n+1):
        for comb in combinations(arr, i):
            if len(comb) == 0:
                continue
            result.append(sum(comb))
    
    return result

N, S = map(int, sys.stdin.readline().split())
mylist = list(map(int, sys.stdin.readline().split()))

mid = N // 2
left = mylist[:mid]
right = mylist[mid:]

leftsum = com(left)
rightsum = com(right)
rightsum.sort()

count = 0

for s in leftsum:
    remain = S - s

    l = bisect_left(rightsum, remain)
    r = bisect_right(rightsum, remain)

    count += (r-l)

count += leftsum.count(S)
count += rightsum.count(S)

print(count)