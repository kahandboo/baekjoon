import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N 

for i in range(len(A)):
    dp[i] = A[i]
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])

print(max(dp))