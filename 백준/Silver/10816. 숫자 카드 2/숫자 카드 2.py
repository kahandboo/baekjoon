n=int(input())
input_n = input().split()
n_d = {}
for num in input_n:
    num = int(num)
    n_d[num]=n_d.get(num, 0) +1
m = int(input())
mm = list(map(int,input().split()))
re=[]

for i in mm:
    if i in n_d:
        re.append(n_d[i])
    else:
        re.append(0)



print(*re)