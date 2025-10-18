def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    camera = routes[0][1]
    print(routes)
        
    for start, end in routes[1:]:
        if start > camera:
            camera = end
            answer += 1
    return answer