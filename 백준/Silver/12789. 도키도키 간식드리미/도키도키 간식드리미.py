import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
waiting = []
count = 1

for i in data:
    while waiting and waiting[-1] == count:
        waiting.pop()
        count += 1
    if i == count:
        count += 1
    else:
        waiting.append(i)

while waiting and waiting[-1] == count:
    waiting.pop()
    count += 1


sys.stdout.write('Nice') if not waiting else sys.stdout.write('Sad')
        
    
    
