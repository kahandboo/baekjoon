import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

memo = [float('inf')] * (K+1)
memo[0] = 0

for i in range(1, K+1):
    for coin in coins:
        if i >= coin:
            memo[i] = min(memo[i], memo[i-coin] + 1)

print(-1 if memo[K] == float('inf') else memo[K])