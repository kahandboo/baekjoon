a, b, c = map(int,input().split())

l = [a,b,c]

x = max(l)
if x < sum(l) - x:
    print(sum(l))
else:
    while x >= sum(l) - max(l):
        x -= 1
    print(sum(l)-max(l)+x)
