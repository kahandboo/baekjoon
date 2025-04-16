import sys

T = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))

max_val = -float('inf')
curr_sum = 0

for i in N:
    curr_sum += i

    if curr_sum > max_val:
        max_val = curr_sum

    if curr_sum < 0:
        curr_sum = 0
    

sys.stdout.write(str(max_val))