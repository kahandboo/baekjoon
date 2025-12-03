import sys
N = int(input())
coordinate = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))

left = 0
right = 0
total = 0

for n in range(N):
    if n == N-1:
        left += coordinate[n][0] * coordinate[0][1]
        right += coordinate[n][1] * coordinate[0][0]
    else:
        left += coordinate[n][0] * coordinate[n+1][1]
        right += coordinate[n][1] * coordinate[n+1][0]

total = abs(left - right)/2

print(f"{total:.1f}")