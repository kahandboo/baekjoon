N = int(input())
answer = [1]
prev = 1
isPlus = True

for i in range(N-1, 0, -1):
    if isPlus:
        answer.append(prev + i)
        isPlus = False
        prev += i
    else:
        answer.append(prev - i)
        isPlus = True
        prev -= i

print(*answer)