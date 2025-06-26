import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    currnum = A[i]
    for j in range(0, i):
        if A[j] < currnum:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))