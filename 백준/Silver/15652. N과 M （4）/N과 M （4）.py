import sys

def backtrack(path):
    if len(path) == M:
        result.extend(path)
        return

    for i in range(1, N+1):
        if path and path[-1] > i:
            continue
        path.append(i)
        backtrack(path)
        path.pop()

N, M = map(int, sys.stdin.readline().split())

result = [] 

backtrack([])


for i in range(0, len(result), M):
    sys.stdout.write(' '.join(map(str, result[i:i+M])) + '\n')
