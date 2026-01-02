import sys
input = sys.stdin.readline
sch = []

N = int(input())
for _ in range(N):
    t, p = map(int, input().split())
    sch.append((t, p))

def solve(day):
    if day >= N:
        return 0
    
    res = solve(day + 1)

    if day + sch[day][0] <= N:
        res = max(res, sch[day][1] + solve(day + sch[day][0]))
    
    return res

print(solve(0))