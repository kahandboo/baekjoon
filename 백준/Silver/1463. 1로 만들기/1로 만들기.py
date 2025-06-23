import sys
sys.setrecursionlimit(10**6)

def dp(x):

    if x%3 == 0:
        if memo[x//3] == -1 or memo[x//3] > memo[x] + 1:
            memo[x//3] = memo[x] + 1
            dp(x//3)
    if x%2 == 0:
        if memo[x//2] == -1 or memo[x//2] > memo[x] + 1:
            memo[x//2] = memo[x] + 1
            dp(x//2)
    if x-1 > 0:
        if memo[x-1] == -1 or memo[x-1] > memo[x] + 1:
            memo[x-1] = memo[x] + 1
            dp(x-1)

    

n = int(sys.stdin.readline())
memo = [-1] * (n+1)
memo[n] = 0

dp(n)

sys.stdout.write(str(memo[1]))
