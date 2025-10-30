import sys
sys.setrecursionlimit(10*6)
n = int(input())

if n == 1:
    print(0)
    print(1)
    sys.exit()
elif n <= 3:
    print(1)
    print(n,1)
    sys.exit()
prev = [0] * (n+1)
dp = [0] * (n+1)

prev[2] = 1
prev[3] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1


for i in range(4, n+1):
    candidates = [(dp[i-1], i-1)]
    if i % 2 == 0:
        candidates.append((dp[i//2], i//2))
    if i % 3 == 0:
        candidates.append((dp[i//3], i//3))
    
    best_val, prev_choice = min(candidates, key=lambda x: x[0])
    dp[i] = best_val + 1
    prev[i] = prev_choice

print(dp[n])
path = []

cur = n
while cur != 0:
    path.append(cur)
    cur = prev[cur]

print(*path)