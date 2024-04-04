n = int(input())
r = []
for _ in range(n):
    r.append(list(map(int,input().split())))

r.sort()
for i in r:
    print(*i)
        
