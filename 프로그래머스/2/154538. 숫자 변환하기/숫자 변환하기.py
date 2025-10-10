from collections import deque
def solution(x, y, n):
    visited = [-1] * (10**6 + 1)
    queue = deque([x])
    visited[x] = 0

    while queue:
        curr = queue.popleft()
        
        if curr == y:
            break
        
        if curr + n < len(visited) and visited[curr+n] == -1:
            visited[curr+n] = visited[curr] + 1
            queue.append(curr+n)
        if curr * 2 < len(visited) and visited[curr*2] == -1:
            visited[curr*2] = visited[curr] + 1
            queue.append(curr*2)
        if curr * 3 < len(visited) and visited[curr*3] == -1:
            visited[curr*3] = visited[curr] + 1
            queue.append(curr*3)
               
    return visited[y]