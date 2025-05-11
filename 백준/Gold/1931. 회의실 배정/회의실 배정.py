import sys

N = int(input())
list = []


for _ in range(N):
    list.append(tuple(map(int, sys.stdin.readline().split())))

list.sort(key=lambda x: (x[1], x[0]))
        
count = 0
endtime = 0

for start, end in list:
    if start >= endtime:
        count += 1
        endtime = end

print(count)