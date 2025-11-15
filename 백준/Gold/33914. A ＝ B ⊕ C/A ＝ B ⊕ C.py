import math

x, y = map(int, input().split())
total = x+y
answer = 0

if x % 2 == 0:
    case1 = (x//2)
    y -= case1

    if y % 3 == 0:
        case2 = y//3
        answer = (3**(case1)) * math.comb(case1 + case2, case1)

print(answer%1000000007)