import sys
sys.setrecursionlimit(10**6)

def dp(floor, idx):
    if floor == n:
        return 0

    if (floor, idx) in memo:
        return memo[(floor, idx)]

    curr = triangle[floor][idx]
    left = dp(floor+1, idx)
    right = dp(floor+1, idx+1)

    memo[(floor, idx)] = max(left, right) + curr
    return memo[(floor, idx)]

n = int(sys.stdin.readline())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

memo = {}

sys.stdout.write(str(dp(0, 0)))
