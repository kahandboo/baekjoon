def solution(elements):
    n = len(elements)
    result = set()
    
    sums = [[0] * n for _ in range(n-1)]
    sums[0] = elements
    
    for i in range(n-1):
        for j in range(n):
            if (i==0):
                result.add(sums[i][j])
            else:
                sums[i][j] = sums[i-1][j] + sums[0][(j+i) % n]
                result.add(sums[i][j])   
            
    result.add(sum(elements))
    
    return len(result)