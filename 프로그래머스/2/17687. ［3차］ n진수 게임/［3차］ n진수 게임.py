def solution(n, t, m, p):
    def transition(base, n):
        if n == 0:
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        while n > 0:
            res.append(digits[n % base])
            n //= base
        return "".join(reversed(res))
    answer = ''
    base = p
    idx = [base-1]
    
    for _ in range(t-1):
        base += m
        idx.append(base - 1)
        
    numbers = ""
    for i in range(t*m):
        numbers += transition(n, i)
    
    for i in idx:
        answer += numbers[i]
    return answer