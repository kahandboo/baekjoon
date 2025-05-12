import sys

N = int(input())

P = list(map(int, sys.stdin.readline().split()))
P.sort()

result = 0
prev = 0

for p in P:
    result += p + prev
    prev += p

print(result)