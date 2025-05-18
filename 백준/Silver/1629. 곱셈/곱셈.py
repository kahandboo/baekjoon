import sys

def f(a, b):
    global C
    if b == 1:
        return a % C
    
    tmp = f(a, b//2)
    
    if b%2 == 0:
        return tmp * tmp % C
    else:
        return tmp * tmp * a % C


A, B, C = map(int, sys.stdin.readline().split())

print(f(A, B))