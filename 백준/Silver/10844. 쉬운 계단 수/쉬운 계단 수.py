import sys

def dp(row):
    if row > n-1:
        return
    
    for i in range(10):
        if i == 0:
            memo[row][i] = memo[row-1][i+1]
        elif i== 9:
            memo[row][i] = memo[row-1][i-1]
        else:
            memo[row][i] = memo[row-1][i-1] + memo[row-1][i+1]

    dp(row + 1)


n = int(sys.stdin.readline())
memo = [[0] * 10 for _ in range(n)]

if n == 1:
    print(9)
    sys.exit()

for i in range(1, 10):
    memo[0][i] = 1


dp(1)

print(sum(memo[n-1]) % 10**9)