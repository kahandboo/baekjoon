N = int(input())
W = []

for _ in range(N):
    W.append(list(map(int, input().split())))

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(i, mask):
    if mask == (1 << N) - 1:
        if W[i][0] == 0:
            return float('inf')
        else:
            return W[i][0]
        
    if dp[i][mask] != -1:
        return dp[i][mask]
    
    min_val = float('inf')

    for j in range(N):
        if (not (mask & 1 << j) and W[i][j] !=0 ):
            temp = W[i][j] + dfs(j, mask | (1 << j))

            min_val = min(min_val, temp)

    dp[i][mask] = min_val
    return min_val

print(dfs(0, 1))