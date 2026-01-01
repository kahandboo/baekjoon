import sys
sys.setrecursionlimit(10**9)
N = int(input())
max_val = 10
memo = [[0] * 10 for _ in range(N)]

for i in range(max_val):
    memo[0][i] = 1

def dp(n):
    if n > N-1:
        return
    
    for i in range(max_val):
        for j in range(i, max_val):
            memo[n][i] += memo[n-1][j]
    dp(n+1)
    
dp(1)

print(sum(memo[N-1]) % 10007)