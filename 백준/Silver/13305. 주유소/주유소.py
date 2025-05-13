import sys

N = int(input())
road = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))

oil.pop()
cost = 0
min_oil = min(oil)

for i in range(N-1):
    if oil[i] > min_oil:
        cost += oil[i] * road[i]
    else:
        road = road[i::]
        cost += sum(road) * oil[i]
        break

print(cost)