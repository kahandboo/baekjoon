def solution(dirs):
    move_dict = {
        "U" : (0, 1),
        "D" : (0, -1),
        "R" : (1, 0),
        "L" : (-1, 0)
    }
    visited = set()
    position = (0, 0)
    answer = 0
    
    for dir in dirs:
        dx, dy = move_dict[dir]
        cx, cy = position
        
        nx = cx + dx
        ny = cy + dy
        
        if (nx > 5 or nx < -5 or ny > 5 or ny < -5):
            continue
        
        position = (nx, ny)
        
        if (cx, cy, nx, ny) in visited or (nx, ny, cx, cy) in visited:
            continue
        
        visited.add((cx, cy, nx, ny))
        visited.add((nx, ny, cx, cy))
        answer += 1
    
        
    return answer