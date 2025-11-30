N = int(input())
histogram = []

for _ in range(N):
    histogram.append(int(input()))

stack = []
max_area = 0

for i in range(N):
    while stack and histogram[stack[-1]] > histogram[i]:
        h = histogram[stack.pop()]
        w = i if not stack else i - stack[-1] -1

        max_area = max(max_area, h*w)
    stack.append(i)

while stack:
    h = histogram[stack.pop()]
    w = N if not stack else N - stack[-1] -1

    max_area = max(max_area, h*w)

print(max_area)