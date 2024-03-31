bb = []
while True:
    x,y,z = map(int,input().split())
    if x ==0 and y==0 and z==0:
        break
    aa = [x,y,z]
    bb.append(aa)

for row in bb:
    if max(row) >= sum(row)-max(row):
        print('Invalid')
    else:
        if len(set(row)) == 1:
            print('Equilateral')
        elif len(set(row)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
