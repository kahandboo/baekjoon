def solution(n, k):
    def transition(base, n):
        if n == 0:
            return "0"
        res = []
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while n > 0:
            res.append(digits[ n%base ])
            n //= base
        return "".join(reversed(res))
    
    def isprime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
    
    filtered = []
    number = transition(k, n)
    parts = number.split('0')
    
    for p in parts:
        if p and '0' not in p:
            if isprime(int(p)):
                filtered.append(p)
    
    return len(filtered)