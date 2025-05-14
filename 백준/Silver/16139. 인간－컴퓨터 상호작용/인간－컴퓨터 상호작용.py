import sys

S = list(sys.stdin.readline())
S.pop()

prefix = {}
for i in range(len(S)):
    for chr in range(97, 123):
        count = 0
        if ord(S[i]) == chr:
            count = 1
        if i == 0:
            prefix[(chr, i)] = count
        else:
            prefix[(chr, i)] = prefix[(chr, i-1)] + count

q = int(input())
answers = []
for _ in range(q):
    a, l, r = input().split()
    a = ord(a)
    l = int(l)
    r = int(r)

    if l == 0:
        answer = prefix[(a, r)]
    else:
        answer = prefix[(a, r)] - prefix[(a, l-1)]

    answers.append(answer)

for answer in answers:
    sys.stdout.write(str(answer) + '\n')

