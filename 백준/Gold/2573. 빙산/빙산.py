import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
icebergs = []
q = []

for i in range(N):
    iceberg = list(map(int, input().split()))
    icebergs.append(iceberg)

    for j in range(M):
        if icebergs[i][j] > 0:
            q.append((i, j))

def time_flows(lists):
    visited = set()
    queue = deque(lists)
    new_lists = []

    while queue:
        cx, cy = queue.popleft()

        if (cx, cy) in visited:
            continue
        
        visited.add((cx, cy))
        loss = 0

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx > N-1 or nx < 0 or ny > M-1 or ny < 0:
                continue

            if (nx, ny) in visited:
                continue

            if icebergs[nx][ny] == 0:
                loss += 1
            else:
                queue.append((nx, ny))
        
        icebergs[cx][cy] = icebergs[cx][cy] - loss if icebergs[cx][cy] - loss >= 0 else 0

        if icebergs[cx][cy] > 0:
            new_lists.append((cx, cy))
    
    return new_lists

def count_loaf(lists):
    visited = set()
    queue = deque([lists[0]])

    while queue:
        cx, cy = queue.popleft()

        if (cx, cy) in visited:
            continue
        
        visited.add((cx, cy))

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx > N-1 or nx < 0 or ny > M-1 or ny < 0:
                continue

            if icebergs[nx][ny] != 0:
                queue.append((nx, ny))
    
    return True if len(visited) == len(lists) else False

years = 0

while count_loaf(q):
    q = time_flows(q)

    if not len(q):
        print(0)
        sys.exit()
    else:
        years += 1

print(years)

