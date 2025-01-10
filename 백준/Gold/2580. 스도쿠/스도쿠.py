import sys

input = sys.stdin.readline


def check(row, col, value):
    for i in range(9):
        if (arr[row][i] == value or arr[i][col] == value):
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (arr[i][j] == value):
                return False
    return True


def dfs(row, col):
    if (col == 9):
        dfs(row + 1, 0)
        return

    if (row == 9):
        for line in arr:
            print(*line)
        sys.exit(0)

    if (arr[row][col] == 0):
        for i in range(1, 10):
            if (check(row, col, i)):
                arr[row][col] = i
                dfs(row, col + 1)
        arr[row][col] = 0
        return

    dfs(row, col + 1)


arr = [list(map(int, input().split())) for _ in range(9)]
dfs(0, 0)