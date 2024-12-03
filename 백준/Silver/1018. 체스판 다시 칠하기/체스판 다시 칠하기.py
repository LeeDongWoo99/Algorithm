N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 체스판 패턴 정의
chess_W = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

chess_B = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

# 최소값 초기화
min_paint = float("inf")

# 모든 8x8 체스판을 탐색
for i in range(N - 7):  # 가능한 행 시작점
    for j in range(M - 7):  # 가능한 열 시작점
        paint_W = 0  # W로 시작하는 체스판과의 차이
        paint_B = 0  # B로 시작하는 체스판과의 차이

        # 8x8 체스판 체크
        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != chess_W[x][y]:
                    paint_W += 1
                if board[i + x][j + y] != chess_B[x][y]:
                    paint_B += 1

        # 최소값 갱신
        min_paint = min(min_paint, paint_W, paint_B)
print(min_paint)