import sys
from collections import deque

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

def bfs(x, y):
    
    q = deque([(x,y)])

    while q:
        cx, cy = q.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx > I-1 or ny > I-1:
                continue

            if board[nx][ny] == 0:
                board[nx][ny] = board[cx][cy] + 1
                q.append((nx,ny))

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    I = int(sys.stdin.readline())
    cx, cy = map(int, sys.stdin.readline().split())
    nx, ny = map(int, sys.stdin.readline().split())

    if cx == nx and cy == ny:
        answer.append(0)
    else:
        board = [[0] * I for _ in range(I)]

        bfs(cx, cy)

        answer.append(board[nx][ny])

for ans in answer:
    sys.stdout.write(str(ans) + '\n')