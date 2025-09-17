from collections import Counter
def solution(topping):
    answer = 0
    left = {}
    right = dict(Counter(topping))
    
    for i in range(len(topping)):
        key = topping[i]
        
        left[key] = left.get(key, 0) + 1
        right[key] = right.get(key, 0) - 1
        
        if right[key] == 0:
            del right[key]
        
        if (len(left.keys()) == len(right.keys())):
            answer += 1
    return answer