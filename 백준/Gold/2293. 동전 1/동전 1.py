import sys
sys.setrecursionlimit(10**6)

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coin = int(sys.stdin.readline())

    coins.append(coin)

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]

print(dp[k])