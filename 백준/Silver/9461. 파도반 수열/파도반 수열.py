import sys
sys.setrecursionlimit(10000) 

def f(x):

    if memo[x] != 0:
        return memo[x]
    
    memo[x] = f(x-2) + f(x-3)
    

    return memo[x] 
            

T = int(sys.stdin.readline())

input = []
result = []

for _ in range(T):
    N = int(sys.stdin.readline())
    input.append(N)

memo = [0] * (max(input)+1)
memo[1] = 1
memo[2] = 1
memo[3] = 1

for i in input:
    result.append(f(i))

sys.stdout.write('\n'.join(map(str,result)) + '\n')