a = []
for _ in range(int(input())):
    a.append(int(input()))

b = []
for i in range(1,len(a)):
    b.append(a[i]-a[i-1])

def gcd(x,y):
    while y != 0:
        x, y = y, x % y
    return x
    
x = b[0]

for s in range(1,len(b)):
    x = gcd(x,b[s])

print((sum(b)//x)-len(b))