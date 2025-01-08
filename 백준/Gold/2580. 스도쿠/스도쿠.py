import sys
input = sys.stdin.readline

def possibility(row, col, value):
    for i in range(9):
        if value == arr[row][i]:
            return False

    for i in range(9):
        if value == arr[i][col]:
            return False

    set_row = (row // 3) * 3
    set_col = (col // 3) * 3

    for i in range(set_row, set_row + 3):
        for j in range(set_col, set_col + 3):
            if arr[i][j] == value:
                return False

    return True

def sudoku(row, col):
    if col == 9:
        sudoku(row + 1, 0)
        return

    if row == 9:
        for line in arr:
            print(*line)
        sys.exit(0)

    if arr[row][col] == 0:
        for i in range(1, 10):
            if possibility(row, col, i):
                arr[row][col] = i
                sudoku(row, col + 1)
                arr[row][col] = 0
        return

    sudoku(row, col + 1)



arr = [list(map(int, input().split())) for _ in range(9)]
sudoku(0, 0)