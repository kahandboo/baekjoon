N = int(input())
D = []

for _ in range(N):
    D.append(list(map(int, input().split())))

dp = [-1] * (1 << N)

def dfs(person, mask):
    if person == N:
        return 0
    
    if dp[mask] != -1:
        return dp[mask]
    
    min_val = float('inf')

    for job in range(N):
        if not (mask & (1 << job)):
            temp = D[person][job] + dfs(person + 1, mask | (1 << job))

            min_val = min(min_val, temp)

    dp[mask] = min_val
    return min_val

print(dfs(0, 0))
