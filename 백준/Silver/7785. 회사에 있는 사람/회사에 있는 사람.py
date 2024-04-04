n = int(input())

office = {}

for _ in range(n):
    name, check = input().split()
    if check == 'enter':
        office[name]=True
    else:
        del office[name]

n_name = sorted(office, reverse=True)
for name in n_name:
    print(name)