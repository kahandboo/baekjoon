a=int(input())
b=len(str(a))*9

for n in range(max(0,a-b),a):
    z = sum(int(digit) for digit in str(n))
    if n+z == a:
        print(n)
        break
else:
    print(0)