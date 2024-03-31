angle = []
for _ in range(3):
    angle.append(int(input()))

if angle.count(60) == 3:
    print('Equilateral')

if sum(angle) != 180:
    print('Error')
else:
    if len(set(angle)) == 2:
        print('Isosceles')
    elif len(set(angle)) == 3:
        print('Scalene')