import sys
from collections import deque

N  = int(sys.stdin.readline())

result = deque()
nums = []
hashtable = {}
sum = 0

for i in range(N):
    num = (int(sys.stdin.readline())) 

    if num not in hashtable:
        hashtable[num] = 1
    else:
        hashtable[num] += 1

    sum += num

    nums.append(num)


nums.sort()

result.append(int(sum/N + 0.5) if sum/N >= 0 else int(sum/N - 0.5))
result.append(nums[N//2])

max_arr = set()

max_key, max_val = max(hashtable.items(), key=lambda k: k[1])

for i in nums:
    if (hashtable[i] == max_val):
        max_arr.add(i)

max_arr = sorted(max_arr)

result.append(max_arr[1] if len(max_arr) > 1 else max_arr[0])
result.append(nums[-1] - nums[0])


sys.stdout.write('\n'.join(map(str, result)) + '\n')
