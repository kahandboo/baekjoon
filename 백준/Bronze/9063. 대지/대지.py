g = []
s = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    g.append(a)
    s.append(b)

new_g = max(g)-min(g)
new_s = max(s)-min(s)

print(new_g * new_s)