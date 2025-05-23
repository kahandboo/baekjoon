import sys

def cal(n):
    total_len = 0

    for h in height:
        if h - n >= 0:
            total_len += h - n

    if total_len >= M:
        return True
    else:
        return False

N, M = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(height)

while (left <= right):

    mid = (left + right) // 2

    if cal(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)