import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = []

    for _ in range(n):
        number = input().strip()
        numbers.append(number)

    numbers.sort()

    for i in range(n-1):
        str1 = numbers[i]
        str2 = numbers[i+1]

        if str2.startswith(str1):
            sys.stdout.write('NO' + '\n')
            break
    else:
        sys.stdout.write('YES' + '\n')