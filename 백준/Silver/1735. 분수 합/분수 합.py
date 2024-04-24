
up = list(map(int,input().split()))
down = list(map(int,input().split()))

a = up[1]
b = down[1]

while a%b != 0:
    r = a%b
    a = b
    b = r

re = [(up[0]*up[1]*down[1]//b)//up[1] + (down[0]*up[1]*down[1]//b)//down[1] , up[1]*down[1]//b]

x=re[0]
y=re[1]

while x%y !=0:
    p = x%y
    x = y
    y = p


if y == 1:
    print(*re)
else:
    pp = [i//y for i in re ]
    print(*pp)