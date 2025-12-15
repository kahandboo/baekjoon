import sys

n, k = map(int, input().split())
if n == k:
    print('Impossible')
    sys.exit()

answer = [i for i in range(2, n-k+1)]

answer.append(1)

answer.extend([i for i in range(len(answer) + 1, n+1)])

print(*answer)