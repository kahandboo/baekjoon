import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

memo = [0] * n

for i in range(n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo) + 1)