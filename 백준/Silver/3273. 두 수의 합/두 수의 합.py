import sys

N = int(sys.stdin.readline())
mylist = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

left = 0
right = N-1

ans = 0

mylist.sort()

if N == 1:
    print(0)
    sys.exit()

while (left < right):
    asum = mylist[left] + mylist[right]

    if asum == x:
        ans += 1
        left += 1
    elif asum < x:
        left += 1
    else:
        right -= 1

print(ans)