import sys
input = sys.stdin.readline
nums = [1, 2, 3]

goal = [0] * (1000001)
goal[0] = 1
goal[1] = 1
goal[2] = 2
goal[3] = 4

for i in range(4, 1000001):
    goal[i] = (goal[i-1] + goal[i-2] + goal[i-3]) % 1000000009


T = int(input())
for _ in range(T):
    n = int(input())
    
    sys.stdout.write(str(goal[n]) + '\n')