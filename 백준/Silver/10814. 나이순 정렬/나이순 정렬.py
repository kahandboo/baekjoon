n=int(input())
u=[]
for _ in range(n):
    age , name = input().split()
    u.append((int(age),name))



u.sort(key = lambda x: (x[0],_))

for row in range(n):
    print(*u[row])