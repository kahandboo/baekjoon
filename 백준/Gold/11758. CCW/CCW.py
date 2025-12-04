points = []

for _ in range(3):
    x, y = map(int, input().split())

    points.append((x, y))

s = (points[1][0] - points[0][0])*(points[2][1] - points[0][1]) - (points[1][1] - points[0][1])*(points[2][0] - points[0][0])

if s > 0:
    answer = 1
elif s < 0:
    answer = -1
else:
    answer = 0

print(answer)