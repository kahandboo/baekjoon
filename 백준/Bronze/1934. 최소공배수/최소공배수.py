def minbaesu(a,b):
    while a%b != 0:
        r = a % b
        a = b
        b = r
    return b

re = []

for _ in range(int(input())):
    x,y = map(int,input().split())
    m = minbaesu(x,y)
    re.append(x*y//m)

print(*re,sep='\n')