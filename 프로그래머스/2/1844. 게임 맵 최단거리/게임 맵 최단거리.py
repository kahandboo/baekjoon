from collections import deque
def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    result = [[0] * m for _ in range(n)]
    result[0][0] = 1
    
    def bfs(x, y, visited):
        visited[x][y] = True
        queue = deque([(x, y)])
        
        while queue:
            cx, cy = queue.popleft()
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                    continue
                    
                if maps[nx][ny] == 0:
                    continue
                    
                if not visited[nx][ny]:
                    result[nx][ny] = result[cx][cy] + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                
                
        
    bfs(0, 0, visited)
    
    if result[n-1][m-1] == 0:
        return -1
    else:
        return result[n-1][m-1]
        