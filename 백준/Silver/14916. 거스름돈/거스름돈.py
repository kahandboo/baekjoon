n = int(input())

coins = [2, 5]
memo = [float('inf')] * (n+5)
memo[2] = 1
memo[5] = 1

for i in range(2, n+1):
    for coin in coins:
        if coin <= i:
            memo[i] = min(memo[i-coin] + 1, memo[i])

print(memo[n] if memo[n] != float('inf') else -1)