def to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(plans):
    plans.sort(key=lambda x: x[1])
    stack = []
    ans = []
    n=len(plans)
    for i in range(n):
        if i < n-1:
            if to_minutes(plans[i][1]) + int(plans[i][2]) > to_minutes(plans[i+1][1]):
                stack.append((plans[i][0], to_minutes(plans[i][1]) + int(plans[i][2]) - to_minutes(plans[i+1][1])))
            elif to_minutes(plans[i][1]) + int(plans[i][2]) == to_minutes(plans[i+1][1]):
                ans.append(plans[i][0])
            else:
                ans.append(plans[i][0])
                if stack:
                    goal = to_minutes(plans[i+1][1])
                    curr = to_minutes(plans[i][1]) + int(plans[i][2])
                    
                    while stack:
                        name, remain = stack.pop()
                        
                        if remain < goal - curr:
                            ans.append(name)
                            curr += remain
                        elif remain == goal - curr:
                            ans.append(name)
                            break
                        else:
                            stack.append((name, (curr+remain) - goal))
                            break
        else:
            ans.append(plans[i][0])
            
            while stack:
                name, remain = stack.pop()
                
                ans.append(name)
                
    return ans
                            
                


