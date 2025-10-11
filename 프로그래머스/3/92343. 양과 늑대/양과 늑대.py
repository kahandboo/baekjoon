def solution(info, edges):
    def isSheep(node):
        return info[node] == 0

    def dfs(node, sheep_count, wolf_count, visited, candidates):
        nonlocal answer
        visited = visited.copy()
        candidates = candidates.copy()
        visited.add(node)

        if isSheep(node):
            sheep_count += 1
        else:
            wolf_count += 1

        if wolf_count >= sheep_count:
            return

        answer = max(answer, sheep_count)

        if node in edge_map:
            for child in edge_map[node]:
                candidates.add(child)

        if node in candidates:
            candidates.remove(node)

        for next_node in candidates:
            dfs(next_node, sheep_count, wolf_count, visited, candidates)

    edge_map = {}
    for parent, child in edges:
        edge_map.setdefault(parent, []).append(child)

    answer = 0
    dfs(0, 0, 0, set(), set())

    return answer
