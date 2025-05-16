import sys

N, M = map(int, input().split())
n = list(map(int, sys.stdin.readline().split()))
prefix = {}
sum = 0
count = 0

for i in range(N):
    sum += n[i]
    if sum % M == 0:
        count += 1
    else:
        if sum % M in prefix:
            prefix[sum % M] += 1
        else:
            prefix[sum % M] = 1

prefix[0] = count

for key, val in prefix.items():
    count += (prefix[key] * (prefix[key] - 1)) // 2

print(count)


