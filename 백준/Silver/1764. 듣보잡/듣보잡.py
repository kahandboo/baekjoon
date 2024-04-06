n, m = map(int, input().split())
heard = set()
duplicates = set()

for _ in range(n):
    name = input()
    heard.add(name)

for _ in range(m):
    name = input()
    if name in heard:
        duplicates.add(name)

print(len(duplicates))
for name in sorted(duplicates):
    print(name)
