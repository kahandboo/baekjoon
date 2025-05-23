import sys

def cal(n):
    count = 1
    i = 1
    next_addr = mylist[0] + n
   
    while i < N:

        if mylist[i] >= next_addr:
            count += 1
            next_addr = mylist[i] + n
        
        i += 1

    if count >= C :
        return True
    else:
        return False


N, C = map(int, sys.stdin.readline().split())
mylist = []
for _ in range(N):
    i = int(sys.stdin.readline())
    mylist.append(i)

mylist.sort()

left = 1
right = mylist[-1] - mylist[0]


while(left <= right):

    mid = (left + right) // 2

    if cal(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1


print(answer)

