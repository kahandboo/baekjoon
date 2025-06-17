import math

def solution(n,a,b):
    
    round = 1
    
    while True:
        if a==b:
            return round-1
        
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        
        round += 1