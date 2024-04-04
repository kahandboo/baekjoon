n,m=map(int,input().split())
s1=[]
s2=[]
for _ in range(n):
    s1.append(input())
for _ in range(m):
    s2.append(input())

s1_set=set(s1)

count = 0

for i in s2:
    if i in s1_set:
        count +=1

print(count)