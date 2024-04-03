a,b,c,d,e,f = map(int,input().split())

de = a*e - b*d

x = (c*e-f*b)//de
y = (a*f-d*c)//de

print(x,y)