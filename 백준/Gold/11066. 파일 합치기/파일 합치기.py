import sys

def getPartSum(l, r):
    if l == 0:
        return sumfile[r]
    else:
        return sumfile[r] - sumfile[l-1]

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    K = int(sys.stdin.readline())

    fileSize = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * K for _ in range(K)]
    opt = [[0] * K for _ in range(K)]
    
    for i in range(K):
        opt[i][i] = i

    sumfile = []
    arr = 0

    for i in range(len(fileSize)):
        arr += fileSize[i]
        sumfile.append(arr)

    for l in range(2, K+1):
        for i in range(0, K-l+1):
            j = i + l - 1
            dp[i][j] = float('inf')

            for k in range(opt[i][j-1], opt[i+1][j]+1):
                if k >= j: break
                cost = dp[i][k] + dp[k+1][j] + getPartSum(i, j)
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    opt[i][j] = k

    answer.append(dp[0][K-1])

for ans in answer:
    sys.stdout.write(str(ans) + '\n')
            


