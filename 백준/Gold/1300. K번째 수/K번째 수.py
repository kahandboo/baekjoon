import sys

def cal(n):

    count = 0
    
    for i in range(1, N + 1):
        count += min(N, n//i)

    if count >= B:
        return True
    else:
        return False

N = int(sys.stdin.readline())
B = int(sys.stdin.readline())

left = 1
right = N*N

while left <= right:

    mid = (left + right) // 2

    if cal(mid):
        answer = mid
        right = mid - 1        
    else:
        left = mid + 1

print(answer)