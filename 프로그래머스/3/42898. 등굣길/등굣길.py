def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    
    for puddle in puddles:
        x, y = puddle
        
        dp[y-1][x-1] = -1
    
    dp[0][0] = 1 

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:  
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    
    
    return dp[n-1][m-1] % 1000000007