import sys

N, M = map(int, input().split())

n = list(map(int, sys.stdin.readline().split()))
prefix = []
sum = 0

for i in range(len(n)):
    sum += n[i]
    prefix.append(sum)

answers = []
for _ in range(M):
    l, r = map(int, input().split())

    if l == 1:
        answers.append(prefix[r-1])
    elif r == l:
        answers.append(n[r-1])
    else:
        answers.append(prefix[r-1] - prefix[l-2])

for answer in answers:
    sys.stdout.write(str(answer) + '\n')

