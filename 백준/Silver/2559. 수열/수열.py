import sys

N, K = map(int, input().split())
temp = list(map(int, sys.stdin.readline().split()))

prefix = []
sum = 0

for i in range(N):
    sum += temp[i]
    prefix.append(sum)

max_sum = prefix[K-1]
j = K

while j < N:
    max_sum = max_sum if max_sum > prefix[j] - prefix[j-K] else prefix[j] - prefix[j-K]
    j += 1

print(max_sum)