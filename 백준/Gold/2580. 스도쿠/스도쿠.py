import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]
zeros = []

for r in range(9):
    for c in range(9):
        num = sudoku[r][c]
        if num == 0:
            zeros.append((r, c))
        else:
            row_check[r][num] = True
            col_check[c][num] = True
            box_check[(r // 3) * 3 + (c // 3)][num] = True

def backtracking(step):
    if step == len(zeros):
        for s in sudoku:
            print(*s)
        sys.exit(0) 
    
    r, c = zeros[step]
    b_idx = (r // 3) * 3 + (c // 3)

    for num in range(1, 10):
        if not row_check[r][num] and not col_check[c][num] and not box_check[b_idx][num]:
            row_check[r][num] = col_check[c][num] = box_check[b_idx][num] = True
            sudoku[r][c] = num
            
            backtracking(step + 1)
            
            row_check[r][num] = col_check[c][num] = box_check[b_idx][num] = False
            sudoku[r][c] = 0

backtracking(0)
