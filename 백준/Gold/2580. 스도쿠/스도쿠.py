import sys
input = sys.stdin.readline

def possible(row, col, value):
    # 행과 열에서 value가 중복되는지 확인
    for i in range(9):
        if value == arr[row][i] or value == arr[i][col]:
            return False

    # 3x3 블록에서 value가 중복되는지 확인
    set_row = (row // 3) * 3
    set_col = (col // 3) * 3
    for i in range(set_row, set_row + 3):
        for j in range(set_col, set_col + 3):
            if arr[i][j] == value:
                return False

    return True

def dfs(row, col):
    # 모든 행을 탐색한 경우 출력 후 종료
    if row == 9:
        for line in arr:
            print(*line)
        sys.exit(0)

    # 새로운 행으로 넘어가는 처리
    if col == 9:
        dfs(row + 1, 0)
        return

    # 빈 칸(0)인 경우 값을 시도
    if arr[row][col] == 0:
        for i in range(1, 10):
            if possible(row, col, i):
                arr[row][col] = i
                dfs(row, col + 1)
                arr[row][col] = 0
    else:
        # 빈 칸이 아닌 경우 다음 열로 이동
        dfs(row, col + 1)

# 입력받기
arr = [list(map(int, input().split())) for _ in range(9)]
dfs(0, 0)
