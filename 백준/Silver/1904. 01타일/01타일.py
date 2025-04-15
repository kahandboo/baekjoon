import sys            

N = int(sys.stdin.readline())
if N==1:
    print(1)
    exit()
elif N==2:
    print(2)
    exit()
memo = [0] * (N+1)
memo[1] = 1
memo[2] = 2

for i in range(3, N+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746


sys.stdout.write(str(memo[N]))