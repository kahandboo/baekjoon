n=int(input())
num1 = set(map(int,input().split()))
m = int(input())
num2 = list(map(int,input().split()))

re=[]
for i in num2:
    if i in num1:
        re.append(1)
    else:
        re.append(0)

print(*re)