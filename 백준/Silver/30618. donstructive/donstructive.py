N = int(input())
num = N
idx = 1
answer = [0] * (N+1)

if N % 2 != 0:
    mid = N//2 + 1
    answer[mid] = num

    while num > 2:
        num -= 1
        answer[mid-idx] = num
        num -= 1
        answer[mid+idx] = num

        idx += 1
else:
    left = N//2
    right = N//2 + 1
    while num > 1:
        answer[left] = num
        num -= 1
        answer[right] = num
        num -= 1

        left -= 1
        right += 1



print(*answer[1:])


