import sys

def getprimes(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]

def partsum(l, r): #부분합 계산
    if l == 0:
        return nums[r]
    else:
        return nums[r] - nums[l-1]

N = int(sys.stdin.readline())
num = getprimes(N) # 소수 배열

nums = [] # 누적합 배열
s = 0

for i in num:
    s += i
    nums.append(s)

ans = 0

left = 0
right = 0

numlen = len(num)
sum = 0

while right < numlen and left <= right:
    
    temp = partsum(left, right)

    if temp == N:
        sum += 1
        left += 1
    elif temp < N:
        right += 1 
    else:
        left += 1

print(sum)