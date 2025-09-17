def solution(arr1, arr2):
    answer = []
    m = len(arr1)
    n = len(arr1[0])
    p = len(arr2[0])
    
    for i in range(m):
        sub = []
        for j in range(p):
            val = 0
            for k in range(n):
                val += arr1[i][k] * arr2[k][j]
            sub.append(val)
        answer.append(sub)
    return answer