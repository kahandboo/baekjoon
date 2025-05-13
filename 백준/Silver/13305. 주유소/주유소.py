import sys

N = int(input())
road = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))

oil.pop()
cost = oil[0] * road[0]
min_oil = oil[0]

for i in range(1, N-1):
    if oil[i] > min_oil:
        cost += min_oil * road[i]
    else:
        min_oil = oil[i]
        cost += min_oil * road[i]

print(cost)