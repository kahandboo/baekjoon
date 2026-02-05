import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    obj = {}
    n = int(input())

    for _ in range(n):
        name, type = input().split()

        if type in obj:
            obj[type].append(name)
        else:
            obj[type] = [name]

    val = 1
    for type in obj:
        val *= (len(obj[type]) + 1)
    
    sys.stdout.write(str(val-1) + '\n')