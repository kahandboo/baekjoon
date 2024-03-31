a = []
for _ in range(3):
    a.append(list(map(int, input().split())))

b = []
c = []
r = []

for i in range(3):
    b.append(a[i][0])
    c.append(a[i][1])

d = []
e = []

for i in range(3):
    d.append(b.count(b[i]))
    if d[i] == 1:
        r.append(b[i])

for i in range(3):
    e.append(c.count(c[i]))
    if e[i] == 1:
        r.append(c[i])

print(*r)

