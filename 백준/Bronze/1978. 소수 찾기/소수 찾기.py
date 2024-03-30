x = int(input())
n = list(map(int,input().split()))


a = []
for i in n:
    s = []
    r = 1
    while r <= i:
        if i%r == 0:
            s.append(r)
        r +=1
    if len(s) == 2:
        a.append(i)

print(len(a))