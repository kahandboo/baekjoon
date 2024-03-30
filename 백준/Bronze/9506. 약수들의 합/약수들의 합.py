s=[]
while True:
    n = int(input())
    if n == -1:
        break
    else:
        s.append(n) 

d= []

for j in s:
    r = []
    i = 1
    while i <= j:
        if j%i == 0:
            r.append(i)
        i += 1
    d.append(r)

for row in d:
    if sum(row[:-1]) == row[-1]:
        print(f"{row[-1]} = {' + '.join(map(str, row[:-1]))}")
    else:
        print(f"{row[-1]} is NOT perfect.")