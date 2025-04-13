import sys



def backtrack(queen):
    global result
    if queen == N:
        result += 1
        return

    for i in range(N):
        if not visited_col[i] and (not visited_diag1[queen-i + N] and not visited_diag2[queen+i]):
            visited_col[i] = True
            visited_diag1[queen-i + N] = True
            visited_diag2[queen+i] = True
            newqueen = queen + 1

            backtrack(newqueen)

            visited_col[i] = False
            visited_diag1[queen-i + N] = False
            visited_diag2[queen+i] = False

                
result = 0

N = int(sys.stdin.readline())

visited_col = [False] * N
visited_diag1 = [False] * 2 * N 
visited_diag2 = [False] * 2 * N

queen = 0


backtrack(queen)


sys.stdout.write(str(result))
