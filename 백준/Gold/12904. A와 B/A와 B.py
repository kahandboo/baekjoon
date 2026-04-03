S = input()
T = input()

idx = len(T) - 1
while len(S) < len(T):
    t = T[idx]
    if t == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
        
    idx -= 1

if T == S:
    print(1)
else:
    print(0)