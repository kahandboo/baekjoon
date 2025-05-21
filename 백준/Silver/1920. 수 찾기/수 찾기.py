import sys

def search(target):
    left = 0
    right = N-1

    while left <= right:
        
        mid = (left + right) // 2

        if A[mid] == target:
            return 1
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        
    return 0

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

A.sort()

answer = []

for val in m:
    answer.append(search(val))

for a in answer:
    sys.stdout.write(str(a) + '\n')
