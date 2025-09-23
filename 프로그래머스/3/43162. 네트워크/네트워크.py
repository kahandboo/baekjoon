def solution(n, computers):
    answer = 0
    visited = n * [False]
    
    def dfs(m, visited):
        visited[m] = True
        for i in range(n):
            if i == m:
                continue

            if computers[m][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i, visited)
        
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, visited)
                
    return answer