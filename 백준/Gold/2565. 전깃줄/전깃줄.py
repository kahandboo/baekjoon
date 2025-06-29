import sys

N = int(sys.stdin.readline())
wires = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    wires.append((a,b))

wires.sort(key=lambda x:x[0])
dp = [1] * 501

for i in range(len(wires)):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[wires[i][1]] = max(dp[wires[i][1]], dp[wires[j][1]] + 1)


print(N - max(dp))