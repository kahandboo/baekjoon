n = int(input())

p = [True] * (n+1)
p[0] = p[1] = False

for i in range(2,int(n**0.5)+1):
    if p[i]:
        for j in range(i**2, n+1 , i):
            p[j] = False
p = [i for i in range(n+1) if p[i]]
r = []
if not n == 1:
    for i in p:
            while n % i == 0:
                  r.append(i)
                  n //= i 
                

for i in r:
    print(i)

