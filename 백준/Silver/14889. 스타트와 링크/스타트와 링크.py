import sys

def backtrack(team):
    if len(team) == N//2:
        team_sum = 0
        other_sum = 0
        other_team = set(range(N)) - set(team)

        for i in team:
            for j in team:
                if (i!=j):
                    team_sum += S[i][j]
        
        for i in other_team:
            for j in other_team:
                if (i!=j):
                    other_sum += S[i][j]

        result.append(abs(team_sum - other_sum))
        return

    for i in range(N):
        if team and team[-1] >= i:
            continue
        team.append(i)
        backtrack(team)
        team.pop()

N = int(sys.stdin.readline())
S= []
for _ in range(N):
    S.append(list(map(int ,sys.stdin.readline().split())))

result = []
team = []

backtrack(team)


sys.stdout.write(str(min(result)))
