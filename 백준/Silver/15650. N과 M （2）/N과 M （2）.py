import sys

def backtrack(path, vistied):
    if len(path) == M:
        result.extend(path)
        return

    for i in range(1, N+1):
        if not vistied[i]:
            if path and path[-1] > i:
                continue
            else:
                visited[i] = True
                path.append(i)
                backtrack(path, visited)
                path.pop()
                visited[i] = False

N, M = map(int, sys.stdin.readline().split())

result = [] 
visited = [False] * (N+1)

backtrack([], visited)


for i in range(0, len(result), M):
    sys.stdout.write(' '.join(map(str, result[i:i+M])) + '\n')
