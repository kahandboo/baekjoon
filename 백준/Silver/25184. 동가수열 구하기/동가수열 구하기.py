N = int(input())
A = [i for i in range(1, N+1)]

answer = [0] * N

idx = N//2

left = A[:idx]
right = A[idx:]

for i in range(0, N-1, 2):
    answer[i] = right[i//2]
    answer[i + 1] = left[i//2]

if N % 2 != 0:
    answer[-1] = N
print(*answer)
