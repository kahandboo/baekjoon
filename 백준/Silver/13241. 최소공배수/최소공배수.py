def minbaesu(a,b):
    while a%b != 0:
        r = a % b
        a = b
        b = r
    return b



x,y = map(int,input().split())
m = minbaesu(x,y)

print(x*y//m)