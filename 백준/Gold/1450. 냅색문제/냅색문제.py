import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

def com(arr):
    n = len(arr)
    result = []

    for i in range(n+1):
        for comb in combinations(arr, i):
            result.append(sum(comb))
    
    return result

N, C = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))


mid = N // 2
left = weights[:mid]
right = weights[mid:]

leftsum = com(left)
rightsum = com(right)
rightsum.sort()

count = 0
for s in leftsum:
    remain = C - s
    r = bisect_right(rightsum, remain)

    count += r


print(count)
