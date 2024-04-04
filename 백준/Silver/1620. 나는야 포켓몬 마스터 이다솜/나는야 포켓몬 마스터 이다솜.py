n,m = map(int,input().split())
poke_name={}
poke_num={}
for i in range(1,n+1):
    name = input()
    poke_name[name]=i
    poke_num[i]=name
re = []
for _ in range(m):
    a=input() 
    if a in poke_name:
        re.append(poke_name[a]) 
    elif int(a) in poke_num:
        re.append(poke_num[int(a)])


for i in re:
    print(i)