import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    coins = list(map(int, input().split()))
    M = int(input())

    goal = [0] * (M+1)
    goal[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            goal[i] += goal[i-coin]

    sys.stdout.write(str(goal[M]) + '\n')