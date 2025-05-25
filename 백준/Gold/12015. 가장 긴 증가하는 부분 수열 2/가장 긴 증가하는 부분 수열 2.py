import sys
  

A = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))

left = 0
right = A - 1
result = []

for i in A_list:

    if not result or result[-1] < i:
        result.append(i)
    else:
        left = 0
        right = len(result) - 1

        while left <= right:
            mid = (left + right) // 2

            if result[mid] >= i:
                right = mid - 1
            else:
                left = mid + 1

        result[left] = i
                 
print(len(result))