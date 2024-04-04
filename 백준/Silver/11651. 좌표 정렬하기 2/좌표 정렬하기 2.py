n = int(input())
r = []
for _ in range(n):
    r.append(list(map(int,input().split())))

r.sort(key = lambda x: (x[1],x[0]))
for i in r:
    print(*i)
        
