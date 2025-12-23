import sys
sys.setrecursionlimit(10**6)

M, N = map(int, sys.stdin.readline().split())
maps = []
dp = [[-1] * N for _ in range(M)] # 경로갯수

for _ in range(M):
    maps.append(list(map(int, sys.stdin.readline().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if r == M-1 and c == N-1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < M and 0 <= nc < N:
            if maps[nr][nc] < maps[r][c]:
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]

print(dfs(0, 0))

