import sys

n = int(sys.stdin.readline())
mylist = list(map(int, sys.stdin.readline().split()))

left = 0
right = n-1
mylist.sort()
cost = abs(mylist[left] + mylist[right])
ans = (mylist[left], mylist[right])

while left < right:
    if abs(mylist[left] + mylist[right]) < cost:
        cost = abs(mylist[left] + mylist[right])
        ans = (mylist[left], mylist[right])

    if mylist[left] + mylist[right] < 0:
        left += 1
    elif mylist[left] + mylist[right] > 0:
        right -= 1
    else:
        print(*(mylist[left], mylist[right]))
        sys.exit()

print(*ans)
