import sys, math
input = sys.stdin.readline

N = int(input())
memo = [i for i in range(N+1)]

for i in range(1, N+1):
    j = 1
    while j*j <= i:
        if memo[i] > memo[i-j*j] + 1:
            memo[i] = memo[i-j*j] + 1
        j += 1

print(memo[N])