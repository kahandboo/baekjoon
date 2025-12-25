import sys

N, M = map(int, input().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

dp = [-1] * (N * 100 + 1)
dp[0] = 0

for i in range(N):
    c = cost[i]
    m = memory[i]
    for j in range(N*100, c-1, -1):
        if dp[j-c] != -1:
            dp[j] = max(dp[j], dp[j-c] + m)

for i in range(len(dp)):
    if (dp[i] >= M):
        print(i)
        break

