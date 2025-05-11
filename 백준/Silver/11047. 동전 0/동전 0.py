import sys

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.reverse()
min_count = 0

for coin in coins:
    if coin <= K:
        min_count += K//coin
        K %= coin
        

print(min_count)