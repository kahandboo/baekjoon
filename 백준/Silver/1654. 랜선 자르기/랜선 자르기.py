import sys

def check(n):
    count = 0

    for len in k:
        count += len // n

    if count >= N:
        return True
    else:
        return False    

K, N = map(int, sys.stdin.readline().split())
k = []

for _ in range(K):
    k.append(int(sys.stdin.readline()))

k.sort()
left = 1
right = k[-1]
answer = 0

while left <= right:

    mid = (left + right) // 2
    
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        

print(answer)