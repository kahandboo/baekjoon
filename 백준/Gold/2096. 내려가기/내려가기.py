import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
max_dp = number[:]
min_dp = number[:]

for _ in range(N-1):
    numbers = list(map(int, input().split()))

    max_0 = numbers[0] + max(max_dp[0], max_dp[1])
    max_1 = numbers[1] + max(max_dp[0], max_dp[1], max_dp[2])
    max_2 = numbers[2] + max(max_dp[2], max_dp[1])

    max_dp[0] = max_0
    max_dp[1] = max_1
    max_dp[2] = max_2

    min_0 = numbers[0] + min(min_dp[0], min_dp[1])
    min_1 = numbers[1] + min(min_dp[0], min_dp[1], min_dp[2])
    min_2 = numbers[2] + min(min_dp[2], min_dp[1])
    
    min_dp[0] = min_0
    min_dp[1] = min_1
    min_dp[2] = min_2

print(max(max_dp), min(min_dp))