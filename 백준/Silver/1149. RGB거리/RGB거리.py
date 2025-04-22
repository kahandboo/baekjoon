import sys

sys.setrecursionlimit(10**6)

def dp(n, curr_cost, prev_color):
    key = (n, prev_color)
    if key in memo:
        return memo[key] + curr_cost  

    if n == N:
        return curr_cost

    min_cost = float('inf')

    for i in range(3):
        if prev_color == i:
            continue
        else:
            curr_color = i

        new_cost = curr_cost + cost[n][i]
        min_cost = min(dp(n+1, new_cost, curr_color), min_cost)

    memo[key] = min_cost - curr_cost  
    return min_cost

N = int(sys.stdin.readline())

cost = []

for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

memo = {}
sys.stdout.write(str(dp(0, 0, -1)))
