from collections import deque
N, L = map(int, input().split())
A = list(map(int, input().split()))

D = deque([])
answer = []

for i in range(N):
    idx = 0 if i-L+1 < 0 else i-L+1
    val = A[i]

    while D and D[-1][0] > val:
        D.pop()

    while D and D[0][1] < idx:
        D.popleft()

    D.append((val, i))
    answer.append(D[0][0])

    

print(*answer)