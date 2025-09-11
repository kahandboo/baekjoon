from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    if cacheSize == 0:
        return len(cities)*5
    
    for rawCity in cities:
        city = rawCity.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            if q and len(q) == cacheSize:
                q.popleft()
            answer += 5
            q.append(city)

    return answer