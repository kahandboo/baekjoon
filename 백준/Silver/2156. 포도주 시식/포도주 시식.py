import sys

n = int(sys.stdin.readline())
wines = [0] * (n+1)
for i in range(1, n+1):
    wines[i] = int(sys.stdin.readline())

dp = [0] * (n+1)

dp[1] = wines[1]
if n>= 2:
    dp[2] = wines[2] + wines[1]

for i in range(3, n+1):
    dp[i] = max(
        dp[i - 1],
        dp[i - 2] + wines[i],
        dp[i - 3] + wines[i-1] + wines[i]
    )

print(dp[n])