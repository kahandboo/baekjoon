re = []
for _ in range(5):
    re.append(int(input()))

re.sort()
print(sum(re)//len(re))
print(re[2])