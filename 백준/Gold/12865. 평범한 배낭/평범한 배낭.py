import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0] * (K + 1)
weight = []
value = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())

    weight.append(W)
    value.append(V)

for i in range(N):
    for w in range(K, weight[i]-1,-1):
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])


print(dp[K])